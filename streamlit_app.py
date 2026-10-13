import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [8.0, 9.0, 7.5, 8.5, 7.0, 6.0, 9.0, 7.0, 8.0, 9.5],
    'Giữa kỳ': [7.0, 8.0, 6.5, 9.0, 7.5, 6.5, 8.5, 7.5, 7.0, 8.5],
    'Cuối kỳ': [8.5, 7.5, 8.0, 8.5, 7.0, 6.0, 9.0, 8.0, 8.5, 9.0]
}
df = pd.DataFrame(data)
df['Tổng kết'] = (0.2 * df['Chuyên cần']) + (0.3 * df['Giữa kỳ']) + (0.5 * df['Cuối kỳ'])

st.subheader("Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

st.subheader("Thống kê chung")
dtk_tb = df['Tổng kết'].mean()
sv_max = df.loc[df['Tổng kết'].idxmax()]
sv_min = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5).sum()

st.write(f"- **Điểm tổng kết trung bình của lớp:** {dtk_tb:.2f}")
st.write(f"- **Sinh viên có điểm tổng kết cao nhất:** {sv_max['Họ và tên']} ({sv_max['Tổng kết']:.2f})")
st.write(f"- **Sinh viên có điểm tổng kết thấp nhất:** {sv_min['Họ và tên']} ({sv_min['Tổng kết']:.2f})")
st.write(f"- **Số sinh viên đạt (điểm tổng kết >= 5):** {so_sv_dat}")

st.subheader("Tra cứu thông tin chi tiết sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Họ và tên'])

student_info = df[df['Họ và tên'] == selected_student].iloc[0]
st.write(f"**Họ và tên:** {student_info['Họ and tên' if 'Họ and tên' in df.columns else 'Họ và tên']}")
st.write(f"**Điểm chuyên cần:** {student_info['Chuyên cần']}")
st.write(f"**Điểm giữa kỳ:** {student_info['Giữa kỳ']}")
st.write(f"**Điểm cuối kỳ:** {student_info['Cuối kỳ']}")
st.write(f"**Điểm tổng kết:** {student_info['Tổng kết']:.2f}")

st.subheader("Biểu đồ cột điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(df['Họ và tên'], df['Tổng kết'], color='skyblue')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Tên sinh viên')
ax.set_xlim(0, 10)
for index, value in enumerate(df['Tổng kết']):
    ax.text(value + 0.2, index, f"{value:.2f}", va='center')
st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<p style='text-align: right; font-size: small; color: gray;'>Họ tên: Nguyễn Đinh Phương Vy - MSSV: 001308059313</p>", 
    unsafe_allow_html=True
)
