import io
import streamlit as st
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

# ==========================================
# 1. إعدادات الصفحة والتصميم المعاصر Modern Glassmorphism Theme
# ==========================================
st.set_page_config(
    page_title="استوديو VIP المعاصر - Youssef Studio",
    page_icon="🎨",
    layout="wide"
)

st.markdown("""
    <style>
    /* خلفية متدرجة معاصرة ومظلمة */
    .stApp {
        background: radial-gradient(circle at top right, #2e1065, #09090b 60%, #030014);
        background-attachment: fixed;
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* كارت الواجهة بتأثير زجاجي مدرج Modern Card Design */
    .glass-header {
        background: rgba(30, 27, 75, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(99, 102, 241, 0.25);
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* شارة المؤسس */
    .founder-badge {
        background: linear-gradient(135deg, #312e81, #4338ca);
        border: 1px solid #6366f1;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-weight: 700;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(67, 56, 202, 0.4);
    }
    
    /* أزرار تفاعلية معاصرة */
    .stButton>button {
        border-radius: 10px !important;
        background: linear-gradient(135deg, #4f46e5, #3b82f6) !important;
        color: white !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. إدارة حالة التأثيرات المحفوظة (Session State)
# ==========================================
if "custom_effects" not in st.session_state:
    st.session_state.custom_effects = {
        "أبيض وأسود عتيق": {"brightness": 1.0, "contrast": 1.0, "grayscale": True, "invert": False, "blur": False, "neon": False, "frame": False},
        "عكس الألوان": {"brightness": 1.0, "contrast": 1.0, "grayscale": False, "invert": True, "blur": False, "neon": False, "frame": False},
        "إضاءة عالية VIP": {"brightness": 1.8, "contrast": 1.3, "grayscale": False, "invert": False, "blur": False, "neon": False, "frame": False},
        "تأثير سينمائي داكن": {"brightness": 0.7, "contrast": 1.6, "grayscale": False, "invert": False, "blur": False, "neon": False, "frame": False},
        "نيون سايبربانك ⚡": {"brightness": 1.4, "contrast": 1.5, "grayscale": False, "invert": False, "blur": False, "neon": True, "frame": True},
    }

# ==========================================
# 3. الشريط الجانبي المعاصر
# ==========================================
with st.sidebar:
    st.markdown('<div class="founder-badge">👑 لوحة المؤسس المتقدمة<br><span style="font-size:11px; color:#cbd5e1; font-weight:400;">Youssef Studio v2026</span></div>', unsafe_allow_html=True)
    
    founder_mode = st.toggle("⚡ وضع المؤسس (التعديل والتخزين)", value=False)
    
    st.divider()
    st.markdown("### 🎨 المكتبة الخاصة بالتأثيرات")
    
    all_effects = list(st.session_state.custom_effects.keys())
    selected_effect = st.selectbox("اختر الفلتر لتطبقه مباشرة:", all_effects)

# ==========================================
# 4. الهيدر الترحيبي
# ==========================================
st.markdown("""
    <div class="glass-header">
        <h2 style="margin: 0; font-size: 26px; font-weight: 800; background: linear-gradient(to right, #a5b4fc, #e0e7ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🎨 استوديو التعديل البصري الخارق</h2>
        <p style="margin: 8px 0 0 0; color: #94a3b8; font-size: 14px;">ارفع صورتك وطبق أحدث التأثيرات الفاخرة مع إمكانية التعديل والتحميل الفوري</p>
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("ارفع الصورة من هاتفك أو جهازك:", type=["jpg", "jpeg", "png", "webp"])

# ==========================================
# 5. منطقة التعديل التفاعلية (معززة بـ st.fragment المعاصرة)
# ==========================================
@st.fragment
def render_studio(image_file):
    original_image = Image.open(image_file)
    processed_image = original_image.copy()

    # --- خيارات القص المعاصرة ---
    with st.expander("✂️ قص وتكييف الأبعاد (للسوشيال ميديا)", expanded=False):
        crop_option = st.segmented_control(
            "اختر الأبعاد المطلوبة:",
            options=["الأصلية", "بروفايل (1:1)", "سناب/تيك توك (9:16)"],
            default="الأصلية"
        )
        w, h = processed_image.size
        if crop_option == "بروفايل (1:1)":
            min_dim = min(w, h)
            left = (w - min_dim) / 2
            top = (h - min_dim) / 2
            processed_image = processed_image.crop((left, top, left + min_dim, top + min_dim))
        elif crop_option == "سناب/تيك توك (9:16)":
            target_h = int(w * 16 / 9)
            if h > target_h:
                top = (h - target_h) / 2
                processed_image = processed_image.crop((0, top, w, top + target_h))

    # --- لوحة المؤسس للتخصيص والحفظ ---
    if founder_mode:
        st.info("🛠️ **أنت الآن في وضع التحكم المباشر للمؤسس:** عدل المؤشرات وسيتحدث المعاين فوراً بدون بطء!")
        
        col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)
        with col_ctrl1:
            b_val = st.slider("السطوع (Brightness):", 0.2, 3.0, 1.2, 0.1)
            c_val = st.slider("التباين (Contrast):", 0.2, 3.0, 1.2, 0.1)
        with col_ctrl2:
            is_gray = st.checkbox("أبيض وأسود")
            is_inv = st.checkbox("عكس الألوان")
            is_neon = st.checkbox("تأثير نيون ⚡")
        with col_ctrl3:
            is_blur = st.checkbox("ضبابية (Blur)")
            is_frame = st.checkbox("إطار VIP 🖼️")
            new_effect_name = st.text_input("اسم التأثير للحفظ:", placeholder="اسم الفلتر الجديد")

        # معالجة التأثيرات المباشرة
        if is_gray:
            processed_image = ImageOps.grayscale(processed_image)
        if is_inv:
            if processed_image.mode == 'RGBA':
                processed_image = processed_image.convert('RGB')
            processed_image = ImageOps.invert(processed_image)
        if is_blur:
            processed_image = processed_image.filter(ImageFilter.BLUR)
        if is_neon:
            processed_image = processed_image.filter(ImageFilter.SHARPEN)
            enhancer_color = ImageEnhance.Color(processed_image)
            processed_image = enhancer_color.enhance(1.8)

        enhancer_b = ImageEnhance.Brightness(processed_image)
        processed_image = enhancer_b.enhance(b_val)
        enhancer_c = ImageEnhance.Contrast(processed_image)
        processed_image = enhancer_c.enhance(c_val)

        if is_frame:
            processed_image = ImageOps.expand(processed_image, border=20, fill='#4f46e5')

        if st.button("💾 حفظ التأثير فوراً للقائمة"):
            if new_effect_name.strip():
                st.session_state.custom_effects[new_effect_name] = {
                    "brightness": b_val, "contrast": c_val,
                    "grayscale": is_gray, "invert": is_inv,
                    "blur": is_blur, "neon": is_neon, "frame": is_frame
                }
                st.toast(f"تم حفظ '{new_effect_name}' بنجاح! 🚀")
                st.rerun()
            else:
                st.warning("يرجى إدخال اسم للتأثير أولاً.")

    # --- تطبيق التأثير الجاهز للمستخدم العادي ---
    else:
        if selected_effect in st.session_state.custom_effects:
            eff_data = st.session_state.custom_effects[selected_effect]
            
            if eff_data["grayscale"]:
                processed_image = ImageOps.grayscale(processed_image)
            if eff_data["invert"]:
                if processed_image.mode == 'RGBA':
                    processed_image = processed_image.convert('RGB')
                processed_image = ImageOps.invert(processed_image)
            if eff_data["blur"]:
                processed_image = processed_image.filter(ImageFilter.BLUR)
            if eff_data["neon"]:
                processed_image = processed_image.filter(ImageFilter.SHARPEN)
                enhancer_color = ImageEnhance.Color(processed_image)
                processed_image = enhancer_color.enhance(1.8)

            enhancer_b = ImageEnhance.Brightness(processed_image)
            processed_image = enhancer_b.enhance(eff_data["brightness"])
            enhancer_c = ImageEnhance.Contrast(processed_image)
            processed_image = enhancer_c.enhance(eff_data["contrast"])

            if eff_data["frame"]:
                processed_image = ImageOps.expand(processed_image, border=20, fill='#4f46e5')

    # --- المعاينة الحديثة جنباً إلى جنب ---
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        st.subheader("📷 الصورة الأصلية")
        st.image(original_image, use_container_width=True)
        
    with col_img2:
        st.subheader(f"✨ الصورة المعدلة: ({selected_effect if not founder_mode else 'معاينة المؤسس'})")
        st.image(processed_image, use_container_width=True)
        
        # حفظ الصورة وتحضيرها للتحميل
        buffered = io.BytesIO()
        save_img = processed_image.convert('RGB') if processed_image.mode in ('RGBA', 'LA', 'P') else processed_image
        save_img.save(buffered, format="JPEG", quality=95)
        
        st.download_button(
            label="📥 تحميل الصورة المعدلة بجودة عالية",
            data=buffered.getvalue(),
            file_name="youssef_studio_export.jpg",
            mime="image/jpeg"
        )

# تشغيل الاستوديو عند رفع الصورة
if uploaded_file is not None:
    render_studio(uploaded_file)
else:
    st.info("💡 قم برفع أي صورة لتبدأ تجربة الاستوديو المعاصر والتعديل الفوري!")
