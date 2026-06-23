import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# ---------------- FIXED MODEL ---------------- #
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()

        self.conv1 = nn.Conv2d(3, 32, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, 3)

        # 🔥 FIX: use Adaptive pooling (NO size issue)
        self.adaptive_pool = nn.AdaptiveAvgPool2d((7, 7))

        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 4)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))

        x = self.adaptive_pool(x)  # 🔥 KEY FIX

        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# ---------------- LOAD MODEL ---------------- #
@st.cache_resource
def load_model():
    try:
        model = torch.load("new_model.pth", map_location="cpu")
        model.eval()
        return model
    except Exception as e:
        st.error(f"❌ Model loading error: {e}")
        return None

    model.eval()
    return model


# ---------------- MAIN APP ---------------- #
def app():
    st.markdown("## 🦠 Crop Disease Detection")
    st.write("Upload a plant leaf image to detect disease")

    model = load_model()

    if model is None:
        return

    uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("🔍 Predict"):

            transform = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
            ])

            img = transform(image).unsqueeze(0)

            try:
                with torch.no_grad():
                    output = model(img)
                    _, predicted = torch.max(output, 1)

                class_names = ["Healthy", "Leaf Spot", "Blight", "Rust"]

                result = class_names[predicted.item()]

                st.success(f"✅ Disease Detected: {result}")

            except Exception as e:
                st.error(f"❌ Error during prediction: {e}")