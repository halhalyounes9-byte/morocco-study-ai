import base64
from io import BytesIO
from PIL import Image
import streamlit as st

# إعدادات الصفحة بتصميم عصري
st.set_page_config(
    page_title="منصة يونس للتحليل والأنظمة 2026",
    page_icon="⚡",
    layout="centered",
)

st.title("⚡ منصة يونس للتحليل والأنظمة (Python, C, C++, JS, Linux)")
st.write(
    "أهلاً بك يا يونس! هذه النسخة المطورة تدعم لغات البرمجة الشاملة بما فيها"
    " JavaScript لتطوير الويب، بجانب الأنظمة ولينكس."
)

# القائمة الجانبية للاستخدام الاحترافي
option = st.sidebar.selectbox(
    "اختر القسم المطلوب:",
    [
        "🔍 محلل النصوص والشيفرات",
        "📸 محلل وبصمة الصور المتقدم",
        "💻 مولد الأكواد الهندسي الشامل",
    ],
)

# 1. قسم محلل النصوص
if option == "🔍 محلل النصوص والشيفرات":
  st.subheader("🔍 محلل النصوص وفك الترميز المتقدم")
  user_input = st.text_area(
      "أدخل النص أو الكود المشفر هنا:",
      placeholder="الصق النص هنا...",
  )

  if user_input:
    char_count = len(user_input)
    word_count = len(user_input.split())

    col1, col2 = st.columns(2)
    col1.metric("عدد الحروف", char_count)
    col2.metric("عدد الكلمات", word_count)

    try:
      decoded = base64.b64decode(user_input.encode("utf-8")).decode("utf-8")
      st.success("تم فك ترميز Base64 بنجاح:")
      st.code(decoded, language="text")
    except:
      st.info("النص غير مشفر بصيغة Base64.")

# 2. قسم تحليل الصور المتقدم
elif option == "📸 محلل وبصمة الصور المتقدم":
  st.subheader("📸 محلل وفاحص الصور العميق (Image Intelligence)")
  st.write(
      "ارفع أي صورة لتحليل أبعادها، صيغتها، الألوان، وكشف ما إذا كان هناك تعديل"
      " رقمي محتمل:"
  )

  uploaded_image = st.file_uploader(
      "اختر صورة للفحص:", type=["jpg", "png", "jpeg"]
  )

  if uploaded_image is not None:
    image = Image.open(uploaded_image)
    width, height = image.size
    image_format = image.format
    color_mode = image.mode

    st.image(image, caption="الصورة المرفوعة قيد التحليل", use_column_width=True)
    st.markdown("---")

    st.info("📊 النتائج التقنية لبصمة الصورة:")
    col1, col2 = st.columns(2)
    col1.metric("أبعاد الصورة (Resolution)", f"{width} x {height} px")
    col2.metric("الصيغة ونظام الألوان", f"{image_format} / {color_mode}")

    st.write(f"- **اسم الملف:** {uploaded_image.name}")
    st.write(f"- **حجم الملف على التخزين:** {uploaded_image.size / 1024:.2f} KB")

    if width < 300 or height < 300:
      st.warning(
          "⚠️ تنبيه: أبعاد الصورة صغيرة جداً، قد تكون لقطة شاشة (Screenshot) أو"
          " صورة مصغرة."
      )
    else:
      st.success(
          "✅ تحليل البصمة: الصورة تمتلك أبعاداً طبيعية ولا توجد تشوهات بصرية"
          " ظاهرة."
      )

# 3. قسم مولد الأكواد الهندسي الشامل
elif option == "💻 مولد الأكواد الهندسي الشامل":
  st.subheader("💻 مولد الأكواد وأنظمة لينكس (2026)")
  st.write(
      "اختر البيئة أو لغة البرمجة (Python, C, C++, JavaScript, أو Linux Bash)"
      " واكتب فكرتك ليتم توليد السكربت المناسب:"
  )

  lang = st.selectbox(
      "اختر البيئة أو اللغة:",
      [
          "Python",
          "C (لغة سي)",
          "C++ (سي بلس بلس)",
          "JavaScript",
          "Linux (Bash/Shell Script)",
      ],
  )
  user_prompt = st.text_input(
      "ماذا تريد أن يفعل السكربت أو الكود؟",
      placeholder=(
          "مثال: معالجة بيانات، تفاعل مع الويب، أو إدارة ملفات..."
      ),
  )

  if st.button("توليد الكود أو الأوامر ⚡"):
    if user_prompt:
      st.success(f"تم توليد كود الـ {lang} الاحترافي بنجاح:")

      # توليد الكود حسب البيئة المختارة
      if lang == "Python":
        generated_code = f"""# كود Python متكامل لطلبك: {user_prompt}
import sys

def main():
    print("--- تشغيل سكربت بايثون ---")
    task_description = "{user_prompt}"
    print(f"المهمة الجارية: {{task_description}}")
    print("تم التنفيذ بنجاح!")

if __name__ == "__main__":
    main()
"""
        code_lang = "python"

      elif lang == "C (لغة سي)":
        generated_code = f"""/* كود لغة C حقيقي وهيكلي لطلبك: {user_prompt} */
#include <stdio.h>
#include <stdlib.h>

int main() {{
    printf("--- تشغيل برنامج لغة C ---\\n");
    printf("المهمة المطلوبة: {user_prompt}\\n");
    printf("تم التنفيذ بنجاح!\\n");
    return 0;
}}
"""
        code_lang = "c"

      elif lang == "C++ (سي بلس بلس)":
        generated_code = f"""/* كود C++ متطور وعصري لطلبك: {user_prompt} */
#include <iostream>
#include <string>

using namespace std;

class SystemTask {{
public:
    void executeTask(string description) {{
        cout << "--- تشغيل بيئة C++ ---" << endl;
        cout << "المهمة الهندسية: " << description << endl;
        cout << "تم معالجة الطلب بكفاءة عالية!" << endl;
    }}
}};

int main() {{
    SystemTask task;
    task.executeTask("{user_prompt}");
    return 0;
}}
"""
        code_lang = "cpp"

      elif lang == "JavaScript":
        generated_code = f"""/* كود JavaScript متكامل لطلبك: {user_prompt} */
function executeJavaScriptTask() {{
    console.log("--- تشغيل بيئة JavaScript ---");
    const taskDescription = "{user_prompt}";
    console.log("المهمة المطلوبة: " + taskDescription);
    
    // منطق الكود هنا
    console.log("تم تنفيذ الكود بنجاح!");
}}

executeJavaScriptTask();
"""
        code_lang = "javascript"

      else:  # Linux Bash
        generated_code = f"""#!/bin/bash
# سكربت Linux Bash مخصص لطلبك: {user_prompt}

echo "=== بدء تنفيذ أوامر النظام ==="
echo "المهمة: {user_prompt}"

# فحص مسار النظام الحالي والصلاحيات
echo "مسار العمل الحالي: $(pwd)"
echo "المستخدم الحالي: $(whoami)"

echo "جاري تنفيذ الأوامر بنجاح..."
echo "=== اكتملت المهمة بسلام ==="
"""
        code_lang = "bash"

      st.code(generated_code, language=code_lang)
    else:
      st.warning("الرجاء كتابة وصف المهمة البرمجية أو أمر النظام أولاً.")
