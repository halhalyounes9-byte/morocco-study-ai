import streamlit as st
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

# ==========================================
# 1. إعدادات الصفحة وتصميم الخلفية (أسود وبنفسجي فاخر)
# ==========================================
st.set_page_config(
    page_title="استوديو التأثيرات - VIP",
    page_icon="🎨",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #09090b, #1e1b4b, #2e1065);
        background-attachment: fixed;
        color: #f8fafc;
    }
    .founder-badge {
        background: linear-gradient(135deg, #1e1b4b, #4338ca);
        border: 1px solid #6366f1;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .stButton>button {
        border-radius: 8px;
        background-color: #4f46e5;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #4338ca;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. إدارة حالة التأثيرات المحفوظة (Session State)
# ==========================================
if "custom_effects" not in st.session_state:
    st.session_state.custom_effects = {
        "أبيض وأسود عتيق": {"brightness": 1.0, "contrast": 1.0, "grayscale": True, "invert": False, "blur": False},
        "عكس الألوان": {"brightness": 1.0, "contrast": 1.0, "grayscale": False, "invert": True, "blur": False},
        "إضاءة عالية VIP": {"brightness": 1.8, "contrast": 1.3, "grayscale": False, "invert": False, "blur": False},
        "تأثير سينمائي داكن": {"brightness": 0.7, "contrast": 1.6, "grayscale": False, "invert": False, "blur": False},
    }

# ==========================================
# 3. الشريط الجانبي: لوحة المؤسس واختيار الفلاتر
# ==========================================
with st.sidebar:
    st.markdown('<div class="founder-badge">👑 لوحة التحكم الخاصة بالمؤسس<br><span style="font-size:11px; color:#cbd5e1;">Developer: يونس 🚀</span></div>', unsafe_allow_html=True)
    
    founder_mode = st.checkbox("⚙️ تفعيل وضع المؤسس (إضافة وتعديل التأثيرات)", value=False)
    
    st.markdown("---")
    st.title("🎨 التأثيرات المتاحة")
    
    all_effects = ["الصورة الأصلية"] + list(st.session_state.custom_effects.keys())
    selected_effect = st.selectbox("اختر التأثير لتطبقه على الصورة:", all_effects)

# ==========================================
# 4. الواجهة الرئيسية
# ==========================================
st.markdown("""
    <div style="background: rgba(30, 27, 75, 0.6); padding: 20px; border-radius: 14px; text-align: center; color: white; margin-bottom: 20px; border: 1px solid #4338ca;">
        <h2 style="margin: 0;">🎨 استوديو تأثيرات الصور الفاخر</h2>
        <p style="margin: 5px 0 0 0; color: #cbd5e1; font-size: 13px;">ارفع صورتك وطبق عليها أقوى الفلاتر والتأثيرات فوراً</p>
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("ارفع الصورة هنا للبدء بالتعديل:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    original_image = Image.open(uploaded_file)
    processed_image = original_image.copy()

    # --- لوحة التحكم الخاصة بالمؤسس عند التفعيل ---
    if founder_mode:
        st.info("🛠️ **وضع المؤسس مفعل:** يمكنك تعديل زوايا الإضاءة والتباين وحفظ هذا التأثير تلقائياً في القائمة!")
        
        col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)
        with col_ctrl1:
            b_val = st.slider("السطوع (Brightness):", 0.2, 3.0, 1.0, 0.1)
            c_val = st.slider("التباين (Contrast):", 0.2, 3.0, 1.0, 0.1)
        with col_ctrl2:
            is_gray = st.checkbox("تحويل لأبيض وأسود")
            is_inv = st.checkbox("عكس الألوان")
        with col_ctrl3:
            is_blur = st.checkbox("تأثير الضبابية (Blur)")
            new_effect_name = st.text_input("اسم التأثير الجديد لتخزينه:", placeholder="مثلاً: فلتر يونس الفخم")

        # تطبيق الإعدادات المباشرة للمؤسس
        if is_gray:
            processed_image = ImageOps.grayscale(processed_image)
        if is_inv:
            if processed_image.mode == 'RGBA':
                processed_image = processed_image.convert('RGB')
            processed_image = ImageOps.invert(processed_image)
        if is_blur:
            processed_image = processed_image.filter(ImageFilter.BLUR)

        # تعديل السطوع والتباين
        enhancer_b = ImageEnhance.Brightness(processed_image)
        processed_image = enhancer_b.enhance(b_val)
        enhancer_c = ImageEnhance.Contrast(processed_image)
        processed_image = enhancer_c.enhance(c_val)

        # زر حفظ التأثير المخصص تلقائياً في القائمة
        if st.button("💾 حفظ التأثير وإضافته تلقائياً للقائمة"):
            if new_effect_name.strip():
                st.session_state.custom_effects[new_effect_name] = {
                    "brightness": b_val,
                    "contrast": c_val,
                    "grayscale": is_gray,
                    "invert": is_inv,
                    "blur": is_blur
                }
                st.success(f"تم حفظ التأثير '{new_effect_name}' وإضافته لقائمة التأثيرات بنجاح! 🚀")
                st.rerun()
            else:
                st.warning("يرجى كتابة اسم للتأثير قبل الحفظ.")

    # --- تطبيق التأثير المختار للمستخدم العادي / عند اختيار تأثير جاهز ---
    else:
        if selected_effect != "الصورة الأصلية" and selected_effect in st.session_state.custom_effects:
            eff_data = st.session_state.custom_effects[selected_effect]
            
            if eff_data["grayscale"]:
                processed_image = ImageOps.grayscale(processed_image)
            if eff_data["invert"]:
                if processed_image.mode == 'RGBA':
                    processed_image = processed_image.convert('RGB')
                processed_image = processed_image.invert(processed_image) if hasattr(ImageOps, 'invert') else ImageOps.invert(processed_image)
            if eff_data["blur"]:
                processed_image = processed_image.filter(ImageFilter.BLUR)

            enhancer_b = ImageEnhance.Brightness(processed_image)
            processed_image = enhancer_b.enhance(eff_data["brightness"])
            enhancer_c = ImageEnhance.Contrast(processed_image)
            processed_image = enhancer_c.enhance(eff_data["contrast"])

    # --- عرض المقارنة (قبل وبعد) ---
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        st.subheader("📷 الصورة الأصلية")
        st.image(original_image, use_column_width=True)
    with col_img2:
        st.subheader(f"✨ النتيجة: ({selected_effect if not founder_mode else 'معاينة وضع المؤسس'})")
        st.image(processed_image, use_column_width=True)

else:
    st.info("💡 ارفع أي صورة لتبدأ باستخدام التعديلات وتجربة وضع المؤسس!")
