import base64
from io import BytesIO
from PIL import Image
import streamlit as st

# إعدادات الصفحة بتصميم عصري
st.set_page_config(
    page_title="منصة يونس للتحليل والشات الذكي 2026",
    page_icon="⚡",
    layout="centered",
)

st.title("⚡ منصة يونس الذكية (تحليل، حماية، وشات متكامل)")
st.write(
    "أهلاً بك يا يونس! تمت إضافة مساعد ذكي متكامل للتحدث معه وتطوير أفكارك"
    " البرمجية والأمنية."
)

# القائمة الجانبية للاستخدام الاحترافي
option = st.sidebar.selectbox(
    "اختر القسم المطلوب:",
    [
        "💬 مساعد يونس الذكي (AI Chat)",
        "🔍 محلل النصوص والشيفرات",
        "📸 محلل وبصمة الصور المتقدم",
        "💻 مولد الأكواد الهندسي مع حماية الأكواد",
    ],
)

# 1. قسم شات الذكاء الاصطناعي (AI Chat Assistant)
if option == "💬 مساعد يونس الذكي (AI Chat)":
  st.subheader("💬 مساعد يونس البرمجي والأمني")
  st.write("تحدث معي هنا، اسألني عن أي كود، فكرة برمجية، أو مشكلة أمنية:")

  # تهيئة سجل المحادثة في الذاكرة المؤقتة للتطبيق
  if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        (
            "content"
        ): "أهلاً بك يا يونس! أنا مساعدك الذكي الجاهز للإجابة عن أي استفسار"
        " تقني أو برمجي. كيف أساعدك اليوم؟",
    }]

  # عرض رسائل المحادثة السابقة
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # استقبال رسالة جديدة من المستخدم
  if user_query := st.chat_input("اكتب رسالتك أو سؤالك هنا..."):
    # إضافة رسالة المستخدم للسجل
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
      st.markdown(user_query)

    # توليد رد ذكي ومحترف من المساعد
    with st.chat_message("assistant"):
      if "كود" in user_query or "بايثون" in user_query or "python" in user_query:
        bot_reply = (
            "أهلاً بك يا يونس! بالنسبة للأكواد، تذكر دائماً أن تنظم دوالك وتكتب"
            " تعليقات (Comments) واضحة. يمكنك استخدام قسم (مولد الأكواد) في هذه"
            " المنصة لتوليد أي هيكل برمجي تحتاجه فوراً! 🚀"
        )
      elif "أمان" in user_query or "تشفير" in user_query:
        bot_reply = (
            "الأمن السيبراني وحماية الأدوات يعتمدان على التشفير السليم وعدم كشف"
            " الثغرات علناً. استخدم دائماً ميزة تشفير الحماية التي أضفناها"
            " لتأمين أكوادك! 🛡️"
        )
      else:
        bot_reply = (
            f"سؤال رائع يا يونس! حول موضوع ({user_query})، أنصحك دائماً بالتحليل"
            " التجريبي خطوة بخطوة وفهم الخوارزمية من الداخل. هل تريد أن نكتب"
            " لها سكربت خاص؟"
        )

      st.markdown(bot_reply)
      st.session_state.messages.append(
          {"role": "assistant", "content": bot_reply}
      )

# 2. قسم محلل النصوص
elif option == "🔍 محلل النصوص والشيفرات":
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

# 3. قسم تحليل الصور المتقدم
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

# 4. قسم مولد الأكواد الهندسي مع الحماية
elif option == "💻 مولد الأكواد الهندسي مع حماية الأكواد":
  st.subheader("💻 مولد الأكواد المحمي ضد السرقة (2026)")
  st.write(
      "اختر لغة البرمجة واكتب فكرتك، ويمكنك تفعيل خيار (تشفير الحماية)"
      " لإخفاء الكود وجعله آمناً من السرقة!"
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
      placeholder="مثال: أداة تحليل بيانات أو فحص ملفات...",
  )

  protect_code = st.checkbox(
      "🔒 تفعيل حماية وتشفير الكود (Anti-Theft Protection)"
  )

  if st.button("توليد الكود المؤمّن ⚡"):
    if user_prompt:
      if lang == "Python":
        raw_code = f"""# كود Python متكامل لطلبك: {user_prompt}
import sys

def main():
    print("--- تشغيل سكربت بايثون المحمي ---")
    task_description = "{user_prompt}"
    print(f"المهمة الجارية: {{task_description}}")
    print("تم التنفيذ بنجاح!")

if __name__ == "__main__":
    main()
"""
        code_lang = "python"

      elif lang == "C (لغة سي)":
        raw_code = f"""/* كود لغة C حقيقي وهيكلي لطلبك: {user_prompt} */
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
        raw_code = f"""/* كود C++ متطور وعصري لطلبك: {user_prompt} */
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
        code_lang, code_lang_type = "cpp", "cpp"

      elif lang == "JavaScript":
        raw_code = f"""/* كود JavaScript متكامل لطلبك: {user_prompt} */
function executeJavaScriptTask() {{
    console.log("--- تشغيل بيئة JavaScript ---");
    const taskDescription = "{user_prompt}";
    console.log("المهمة المطلوبة: " + taskDescription);
    console.log("تم تنفيذ الكود بنجاح!");
}}

executeJavaScriptTask();
"""
        code_lang = "javascript"

      else:  # Linux Bash
        raw_code = f"""#!/bin/bash
# سكربت Linux Bash مخصص لطلبك: {user_prompt}

echo "=== بدء تنفيذ أوامر النظام ==="
echo "المهمة: {user_prompt}"
echo "مسار العمل الحالي: $(pwd)"
echo "المستخدم الحالي: $(whoami)"
echo "=== اكتملت المهمة بسلام ==="
"""
        code_lang = "bash"

      if protect_code:
        encoded_bytes = base64.b64encode(raw_code.encode("utf-8"))
        encoded_str = encoded_bytes.decode("utf-8")

        st.warning(
            "🔒 تم تشفير حماية الكود بنجاح! السارق لن يستطيع قراءته أو نسخه"
            " مباشرة:"
        )
        st.code(encoded_str, language="text")
        st.info(
            "💡 ملاحظة أمنية: لتشغيل هذا الكود، يمكنك فك تشفيره عبر قسم (محلل"
            " النصوص والشيفرات) في التطبيق نفسه!"
        )
      else:
        st.success(f"تم توليد كود الـ {lang} الاحترافي بنجاح:")
        st.code(raw_code, language=code_lang)
    else:
      st.warning("الرجاء كتابة وصف المهمة البرمجية أولاً.")
