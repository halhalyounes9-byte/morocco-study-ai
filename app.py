import io
import streamlit as st
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

# ==========================================
# 1. إعدادات الصفحة والتصميم المعاصر
# ==========================================
st.set_page_config(
    page_title="استوديو التأثيرات الملكي - Youssef VIP",
    page_icon="🎨",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #1e1b4b, #09090b 60%, #030014);
        background-attachment: fixed;
        color: #f8fafc;
        font-family: 'Inter', system-ui, sans-serif;
    }
    .glass-header {
        background: rgba(30, 27, 75, 0.4);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(99, 102, 241, 0.25);
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .founder-badge {
        background: linear-gradient(135deg, #312e81, #4338ca);
        border: 1px solid #6366f1;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-weight: 700;
        margin-bottom: 20px;
    }
    .stButton>button {
        border-radius: 10px !important;
        background: linear-gradient(135deg, #4f46e5, #3b82f6) !important;
        color: white !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 10px 20px !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. مكتبة الـ 100+ تأثير المتنوعة بدقة
# ==========================================
if "effects_library" not in st.session_state:
    st.session_state.effects_library = {
        # --- التأثيرات المميزة (Favorites) ---
        "✨ إضاءة عالية VIP (Bright)": {"b": 1.7, "c": 1.4, "gray": False, "inv": False, "blur": False, "sharp": True, "frame": False},
        "🖤 أبيض وأسود نقي (Pure B&W)": {"b": 1.0, "c": 1.3, "gray": True, "inv": False, "blur": False, "sharp": False, "frame": False},
        "⚡ توهج سايبربانك (Neon Cyber)": {"b": 1.5, "c": 1.6, "gray": False, "inv": False, "blur": False, "sharp": True, "frame": True},
        "🎬 سينمائي داكن (Dark Cinema)": {"b": 0.75, "c": 1.8, "gray": False, "inv": False, "blur": False, "sharp": False, "frame": False},
        "🌌 ضبابية حالمة (Dreamy Blur)": {"b": 1.1, "c": 1.1, "gray": False, "inv": False, "blur": True, "sharp": False, "frame": False},
        "🔄 عكس الألوان الفني (Invert Art)": {"b": 1.0, "c": 1.0, "gray": False, "inv": True, "blur": False, "sharp": False, "frame": False},
    }

    # توليد الـ 100 تأثير المتبقية بقيم متباينة وحقيقية تضمن عدم تكرار شكل الأبيض والأسود
    styles_list = ["سينمائي", "ريترو", "سايبر", "إضاءة ملكية", "تباين حاد", "توهج فني", "كلاسيكي"]
    for i in range(1, 95):
        style_name = styles_list[i % len(styles_list)]
        st.session_state.effects_library[f"فلتر {style_name} #{i}"] = {
            "b": round(0.6 + (i % 25) * 0.08, 2),
            "c": round(0.7 + (i % 20) * 0.09, 2),
            "gray": (i % 12 == 0),  # نسبة قليلة فقط تكون أبيض وأسود
            "inv": (i == 45 or i == 88),
            "blur": (i % 15 == 0),
            "sharp": (i % 3 == 0 or i % 5 == 0),
            "frame": (i % 4 == 0)
        }

# ==========================================
# 3. الشريط الجانبي وتصنيف التأثيرات
# ==========================================
with st.sidebar:
    st.markdown('<div class="founder-badge">👑 لوحة المؤسس الملكية<br><span style="font-size:11px; color:#cbd5e1;">Youssef VIP Studio</span></div>', unsafe_allow_html=True)
    
    founder_mode = st.toggle("⚡ وضع المؤسس (تعديل وإنشاء التأثيرات)", value=False)
    
    st.divider()
    st.markdown("### 🗂️ تصنيفات التأثيرات (Filters Library)")
    
    tab_choice = st.radio("اختر القسم:", ["Favorites المفضلة", "All الكل (100+ تأثير)"])
    
    all_effect_names = list(st.session_state.effects_library.keys())
    
    if tab_choice == "Favorites المفضلة":
        favorite_list = [
            "✨ إضاءة عالية VIP (Bright)",
            "🖤 أبيض وأسود نقي (Pure B&W)",
            "⚡ توهج سايبربانك (Neon Cyber)",
            "🎬 سينمائي داكن (Dark Cinema)",
            "🌌 ضبابية حالمة (Dreamy Blur)",
            "🔄 عكس الألوان الفني (Invert Art)"
        ]
        selected_effect = st.selectbox("اختر من المفضلة:", favorite_list)
    else:
        selected_effect = st.selectbox("اختر من مكتبة الـ 100+ تأثير:", all_effect_names)

# ==========================================
# 4. الواجهة الرئيسية
# ==========================================
st.markdown("""
    <div class="glass-header">
        <h2 style="margin: 0; font-size: 26px; font-weight: 800; background: linear-gradient(to right, #a5b4fc, #e0e7ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🎨 استوديو التأثيرات البصرية المتكامل</h2>
        <p style="margin: 8px 0 0 0; color: #94a3b8; font-size: 14px;">مكتبة تضم أكثر من 100+ تأثير فخم ومختلف لتغيير مظهر صورك فوراً</p>
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("ارفع الصورة من هاتفك أو جهازك:", type=["jpg", "jpeg", "png", "webp"])

# ==========================================
# 5. معالجة وتطبيق التأثيرات
# ==========================================
@st.fragment
def render_studio(image_file):
    original_image = Image.open(image_file)
    processed_image = original_image.copy()

    # --- أداة قص وتكييف الأبعاد ---
    with st.expander("✂️ خيارات قص وتعديل الأبعاد", expanded=False):
        crop_option = st.segmented_control(
            "الأبعاد:",
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

    # --- وضع المؤسس للتعديل المباشر ---
    if founder_mode:
        st.info("🛠️ **وضع المؤسس مفعل:** تحكم بجميع زوايا الإضاءة والتباين وأضف تأثيراتك الجديدة للقائمة!")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            b_val = st.slider("السطوع:", 0.2, 3.0, 1.2, 0.1)
            c_val = st.slider("التباين:", 0.2, 3.0, 1.2, 0.1)
        with col2:
            is_gray = st.checkbox("أبيض وأسود")
            is_inv = st.checkbox("عكس الألوان")
            is_sharp = st.checkbox("حدة عالية (Sharp)")
        with col3:
            is_blur = st.checkbox("ضبابية (Blur)")
            is_frame = st.checkbox("إطار ملكي فاخر 🖼️")
            new_name = st.text_input("اسم التأثير الجديد:")

        if is_gray:
            processed_image = ImageOps.grayscale(processed_image)
        if is_inv:
            if processed_image.mode == 'RGBA':
                processed_image = processed_image.convert('RGB')
            processed_image = ImageOps.invert(processed_image)
        if is_blur:
            processed_image = processed_image.filter(ImageFilter.BLUR)
        if is_sharp:
            processed_image = processed_image.filter(ImageFilter.SHARPEN)

        processed_image = ImageEnhance.Brightness(processed_image).enhance(b_val)
        processed_image = ImageEnhance.Contrast(processed_image).enhance(c_val)

        if is_frame:
            processed_image = ImageOps.expand(processed_image, border=25, fill='#4f46e5')

        if st.button("💾 حفظ وتثبيت التأثير الجديد في المكتبة"):
            if new_name.strip():
                st.session_state.effects_library[new_name] = {
                    "b": b_val, "c": c_val, "gray": is_gray,
                    "inv": is_inv, "blur": is_blur, "sharp": is_sharp, "frame": is_frame
                }
                st.success(f"تمت إضافة '{new_name}' بنجاح إلى مكتبة التأثيرات! 🚀")
                st.rerun()
            else:
                st.warning("يرجى كتابة اسم للتأثير.")

    # --- تطبيق التأثير المختار من القائمة الضخمة للمستخدم العادي ---
    else:
        if selected_effect in st.session_state.effects_library:
            eff = st.session_state.effects_library[selected_effect]
            
            # 1. تطبيق الأبيض والأسود فقط إذا كان مفعلاً في هذا الفلتر بالذات
            if eff["gray"]:
                processed_image = ImageOps.grayscale(processed_image)
            
            # 2. عكس الألوان
            if eff["inv"]:
                if processed_image.mode == 'RGBA':
                    processed_image = processed_image.convert('RGB')
                processed_image = ImageOps.invert(processed_image)
            
            # 3. الضبابية والحدة
            if eff["blur"]:
                processed_image = processed_image.filter(ImageFilter.BLUR)
            if eff["sharp"]:
                processed_image = processed_image.filter(ImageFilter.SHARPEN)

            # 4. السطوع والتباين
            processed_image = ImageEnhance.Brightness(processed_image).enhance(eff["b"])
            processed_image = ImageEnhance.Contrast(processed_image).enhance(eff["c"])

            # 5. الإطار الفاخر
            if eff["frame"]:
                processed_image = ImageOps.expand(processed_image, border=25, fill='#4f46e5')

    # --- عرض النتيجة قبل وبعد ---
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        st.subheader("📷 الصورة الأصلية")
        st.image(original_image, use_container_width=True)
        
    with col_img2:
        st.subheader(f"✨ التأثير: ({selected_effect if not founder_mode else 'معاينة المؤسس'})")
        st.image(processed_image, use_container_width=True)
        
        buffered = io.BytesIO()
        save_img = processed_image.convert('RGB') if processed_image.mode in ('RGBA', 'LA', 'P') else processed_image
        save_img.save(buffered, format="JPEG", quality=95)
        
        st.download_button(
            label="📥 تحميل الصورة المعدلة بجودة عالية",
            data=buffered.getvalue(),
            file_name="youssef_vip_styled.jpg",
            mime="image/jpeg"
        )

if uploaded_file is not None:
    render_studio(uploaded_file)
else:
    st.info("💡 ارفع أي صورة من جهازك لتبدأ بتصفح واختيار تأثيرات مكتبة الـ 100+ فلتر الملكية!")
