import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import os
import time
from typing import Optional, Tuple
import base64
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(
    page_title="AI Image Caption Generator & Editor ",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        .caption-box {
            background-color: #f0f2f6;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            border-left: 5px solid #4e79a7;
        }
        .caption-box p {
            font-size: 1.2rem;
            color: #333;
            margin: 0;
        }
        .stButton>button {
            background-color: #4e79a7;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            border: none;
        }
        .stButton>button:hover {
            background-color: #3a5f8a;
            color: white;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            padding: 8px 16px;
            border-radius: 4px 4px 0px 0px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #4e79a7;
            color: white;
        }
        .edit-param {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .edit-slider {
            margin-top: -15px;
        }
        .feature-card {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .highlight {
            background-color: #fffacd;
            padding: 2px 5px;
            border-radius: 3px;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Cache the model loading to improve performance
@st.cache_resource(show_spinner=False)
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        ).to(device)
        return processor, model, device
    except Exception as e:
        st.error(f"Failed to load model: {str(e)}")
        return None, None, None

# Image editing functions
def rotate_image(image: Image.Image, degrees: int) -> Image.Image:
    return image.rotate(degrees, expand=True)

def crop_image(image: Image.Image, left: int, top: int, right: int, bottom: int) -> Image.Image:
    return image.crop((left, top, right, bottom))

def adjust_brightness(image: Image.Image, factor: float) -> Image.Image:
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image: Image.Image, factor: float) -> Image.Image:
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def flip_image(image: Image.Image, direction: str) -> Image.Image:
    if direction == "Horizontal":
        return ImageOps.mirror(image)
    else:
        return ImageOps.flip(image)

# Caption generation functions
def generate_caption(image: Image.Image, processor, model, device, 
                    text: Optional[str] = None, 
                    max_length: int = 30, 
                    num_beams: int = 5) -> Tuple[str, float]:
    """Generate caption for the given image using BLIP model with timing"""
    try:
        start_time = time.time()
        
# Preprocess the image
        inputs = processor(image, text, return_tensors="pt").to(device)
        
# Generate caption with configurable parameters
        out = model.generate(
            **inputs, 
            max_length=max_length,
            num_beams=num_beams,
            early_stopping=True
        )
        
# Decode the caption
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        processing_time = time.time() - start_time
        return caption, processing_time
    except Exception as e:
        st.error(f"Error generating caption: {str(e)}")
        return "", 0.0

def generate_multiple_captions(image: Image.Image, processor, model, device, 
                             text: Optional[str] = None, 
                             num_captions: int = 3) -> list:
    """Generate multiple diverse captions using nucleus sampling"""
    try:
        inputs = processor(image, text, return_tensors="pt").to(device)
        
# Generate diverse captions
        outputs = model.generate(
            **inputs,
            max_length=30,
            do_sample=True,
            top_p=0.9,
            num_return_sequences=num_captions
        )
        
        captions = [processor.decode(out, skip_special_tokens=True) for out in outputs]
        return captions
    except Exception as e:
        st.error(f"Error generating multiple captions: {str(e)}")
        return []

def image_to_base64(image: Image.Image) -> str:
    """Convert PIL image to base64 string"""
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

def analyze_image(image: Image.Image) -> dict:
    """Perform basic image analysis"""
    grayscale = np.array(image.convert("L"))
    return {
        "brightness": np.mean(grayscale),
        "contrast": np.std(grayscale),
        "edges": "high" if np.std(grayscale) > 25 else "low",
        "dominant_color": get_dominant_color(image)
    }

def get_dominant_color(image: Image.Image) -> str:
    """Get dominant color from image"""
    small_image = image.resize((100, 100))
    colors = small_image.getcolors(10000)
    if colors:
        most_common = max(colors, key=lambda x: x[0])[1]
        return f"RGB({most_common[0]}, {most_common[1]}, {most_common[2]})"
    return "N/A"

def show_model_info(processor, model, device):
    """Display detailed model information"""
    with st.expander("🧠 Model Details", expanded=False):
        st.write(f"**Model Name:** BLIP Image Captioning Base")
        st.write(f"**Framework:** PyTorch")
        st.write(f"**Device:** {device.upper()}")
        st.write(f"**Precision:** {model.dtype}")
        st.write(f"**Parameters:** {sum(p.numel() for p in model.parameters()):,}")
        st.write(f"**Input Size:** {processor.image_processor.size}")
        
# Memory usage
        if device == "cuda":
            mem_alloc = torch.cuda.memory_allocated() / 1024**2
            mem_reserved = torch.cuda.memory_reserved() / 1024**2
            st.write(f"**GPU Memory Allocated:** {mem_alloc:.2f} MB")
            st.write(f"**GPU Memory Reserved:** {mem_reserved:.2f} MB")

def main():
    st.title("Advanced Image Caption Generator")
    st.markdown("""
    <div style="text-align: left; margin-bottom: 20px;">
        <p>Edit your images with advanced tools and generate AI-powered captions with multiple options.</p>
    </div>
    """, unsafe_allow_html=True)
    
# Load model
    with st.spinner("⚙️ Loading Project... Please wait."):
        processor, model, device = load_model()
    
    if processor is None or model is None:
        st.error("Failed to load the model. Please check your internet connection or try again later.")
        return
    
# Sidebar with advanced options
    with st.sidebar:
        st.header("⚙️ Settings")
        
        with st.expander("Caption Generation", expanded=True):
            text_prompt = st.text_input(
                "Context prompt (optional)", 
                placeholder="E.g., 'a picture of' or 'this is'",
                help="Provide some context to guide the caption generation"
            )
            
            max_length = st.slider(
                "Maximum caption length", 
                min_value=10, 
                max_value=50, 
                value=30,
                help="Control how long the generated caption can be"
            )
            
            num_beams = st.slider(
                "Beam search width", 
                min_value=1, 
                max_value=10, 
                value=5,
                help="Higher values produce better but slower results"
            )
            
            num_captions = st.slider(
                "Number of caption variants", 
                min_value=1, 
                max_value=5, 
                value=3,
                help="Generate multiple caption options to choose from"
            )
        
        with st.expander("Image Editing", expanded=True):
            edit_tabs = st.tabs(["Basic", "Adjustments", "Crop"])

# Basic edits           
            with edit_tabs[0]: 
                rotate_deg = st.slider(
                    "Rotation (degrees)", 
                    -180, 180, 0,
                    help="Rotate the image clockwise or counter-clockwise"
                )
                flip_dir = st.selectbox(
                    "Flip Direction", 
                    ["None", "Horizontal", "Vertical"],
                    help="Flip the image horizontally or vertically"
                )

# Adjustments            
            with edit_tabs[1]:  
                brightness = st.slider(
                    "Brightness", 
                    0.5, 1.5, 1.0,
                    help="Adjust image brightness"
                )
                contrast = st.slider(
                    "Contrast", 
                    0.5, 1.5, 1.0,
                    help="Adjust image contrast"
                )

# Crop          
            with edit_tabs[2]:  
                crop_enabled = st.checkbox("Enable Crop", False)
                if crop_enabled:
                    cols = st.columns(4)
                    with cols[0]:
                        left = st.number_input("Left", 0, 1000, 0)
                    with cols[1]:
                        top = st.number_input("Top", 0, 1000, 0)
                    with cols[2]:
                        right = st.number_input("Right", 1, 1000, 800)
                    with cols[3]:
                        bottom = st.number_input("Bottom", 1, 1000, 600)
        
        with st.expander("Display Options", expanded=False):
            show_analysis = st.checkbox("Show image analysis", value=True)
            show_model_details = st.checkbox("Show model details", value=False)
            show_debug = st.checkbox("Show debug info", value=False)


        st.markdown("---")
        st.markdown("""
        **About this app:**
        - Powered by a Vision-Language Transformer model. 
        - Optimized for generating natural image descriptions.
        - Fine-tuned for image captioning.
        - Trained to understand and describe images intelligently.
        - Runs on {'GPU' if device == 'cuda' else 'CPU'}.
        """)


        
        

# Main content area
    col1, col2 = st.columns([1, 1], gap="medium")
    
    with col1:
        st.subheader("🖼️ Image Editor & Upload")
        uploaded_file = st.file_uploader(
            "Choose an image...", 
            type=["jpg", "jpeg", "png", "webp"],
            help="Select an image file to edit and caption",
            label_visibility="collapsed"
        )
        
        if uploaded_file is not None:
            try:
                original_image = Image.open(uploaded_file).convert("RGB")
                edited_image = original_image.copy()
                
# Apply all edits
                with st.spinner("Applying edits..."):
                    if rotate_deg != 0:
                        edited_image = rotate_image(edited_image, rotate_deg)
                    if flip_dir != "None":
                        edited_image = flip_image(edited_image, flip_dir)
                    if brightness != 1.0:
                        edited_image = adjust_brightness(edited_image, brightness)
                    if contrast != 1.0:
                        edited_image = adjust_contrast(edited_image, contrast)
                    if crop_enabled:
                        edited_image = crop_image(edited_image, left, top, right, bottom)
                
# Show edit comparison
                st.subheader("🔄 Edit Comparison")
                compare_cols = st.columns(2)
                with compare_cols[0]:
                    st.image(original_image, caption="Original Image", use_column_width=True)
                with compare_cols[1]:
                    st.image(edited_image, caption="Edited Image", use_column_width=True)
                
# Image analysis section
                if show_analysis:
                    with st.expander("🔍 Image Analysis", expanded=True):
                        analysis = analyze_image(edited_image)
                        
                        col1a, col2a = st.columns(2)
                        with col1a:
                            st.metric("Brightness", f"{analysis['brightness']:.1f}")
                            st.metric("Contrast", f"{analysis['contrast']:.1f}")
                        
                        with col2a:
                            st.metric("Edge Detail", analysis['edges'])
                            st.metric("Dominant Color", analysis['dominant_color'])
                            
# Simple histogram
                            fig, ax = plt.subplots()
                            ax.hist(np.array(edited_image.convert("L")).ravel(), bins=50, color='blue', alpha=0.7)
                            ax.set_title('Pixel Intensity Distribution')
                            st.pyplot(fig)
                
# Debug info
                if show_debug:
                    with st.expander("🐛 Debug Information", expanded=False):
                        st.write(f"Image format: {original_image.format}")
                        st.write(f"Original size: {original_image.size}")
                        st.write(f"Edited size: {edited_image.size}")
                        st.write(f"Image mode: {original_image.mode}")
                
# Save edited image
                buf = BytesIO()
                edited_image.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="💾 Download Edited Image",
                    data=byte_im,
                    file_name="edited_image.jpg",
                    mime="image/jpeg",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")
        else:
            st.info("ℹ️ Please upload an image to begin")
            
    
    with col2:
        st.subheader("📝 Caption Generator")
        
        if uploaded_file is not None and 'edited_image' in locals():
            if st.button("✨ Generate Captions", use_container_width=True):
                with st.spinner("🧠 Generating captions... This may take a moment"):
# Generate primary caption
                    primary_caption, processing_time = generate_caption(
                        edited_image, processor, model, device, 
                        text_prompt, max_length, num_beams
                    )
                    
# Generate multiple caption variants
                    caption_variants = generate_multiple_captions(
                        edited_image, processor, model, device,
                        text_prompt, num_captions
                    )
                
                if primary_caption:
# Display primary caption
                    st.markdown(f"""
                    <div class="caption-box">
                        <h4 style="color:red;">🌟 Best Caption</h4>
                        <p>{primary_caption}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
# Display caption variants
                    if len(caption_variants) > 1:
                        st.markdown("#### 🔄 Alternative Captions")
                        for i, caption in enumerate(caption_variants[1:], 1):
                            st.markdown(f"""
                            <div class="caption-box" style="border-left-color: #7eb0d5;">
                                <p>{caption}</p>
                            </div>
                            """, unsafe_allow_html=True)
                    
# Performance metrics
                    with st.expander("📊 Performance Metrics", expanded=False):
                        col1b, col2b, col3b = st.columns(3)
                        with col1b:
                            st.metric("Processing Time", f"{processing_time:.2f} seconds")
                        with col2b:
                            st.metric("Caption Length", f"{len(primary_caption.split())} words")
                        with col3b:
                            st.metric("Model Device", device.upper())
                    
# Export options
                    st.markdown("---")
                    st.markdown("#### 💾 Export Options")
                    col1c, col2c = st.columns(2)
                    with col1c:
                        st.download_button(
                            label="Download Caption as TXT",
                            data=primary_caption,
                            file_name="caption.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    with col2c:
# Create a PDF would require reportlab or similar
                        st.button("Save to PDF (Coming Soon)", disabled=True)
                
                else:
                    st.warning("Could not generate captions. Please try another image.")
            
# Model information
            if show_model_details:
                show_model_info(processor, model, device)
        else:
            st.info("Upload and edit an image first, then generate captions here")

# Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <p>𝐂𝐨𝐝𝐢𝐧𝐠 𝐒𝐚𝐦𝐮𝐫𝐚𝐢 𝐈𝐧𝐭𝐞𝐫𝐧 AI Image Caption Generator & Editor </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()