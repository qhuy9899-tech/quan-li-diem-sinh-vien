import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#7. Tao du lieu sinh vien
data={
    "Ho_va_ten": ["A","K","I","H","G","F","E","D","B","C"],
    "Chuyen_can":[10, 9, 8, 7, 8, 9, 10, 10, 7, 9],
    "Giua_ky": [8, 8, 8, 8, 8, 8, 8, 9, 9, 10],
    "Cuoi_ky": [10, 9, 8, 8, 9, 9, 7, 10, 8, 9]
}
df= pd.DataFrame(data)
print("BANG DIEM BAN DAU:")
# Tinh diem tong ket

df["Tong_ket"] = (

    0.2 * df["Chuyen_can"]

    + 0.3 * df["Giua_ky"]

    + 0.5 * df["Cuoi_ky"]

)

# Xep loai

def xep_loai(diem):

    if diem >= 8.5:

        return "Gioi"

    elif diem >= 7:

        return "Kha"

    elif diem >= 5:

        return "Trung binh"

    return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Tieu de ung dung

st.title("QUAN LY DIEM SINH VIEN")

# Bang diem

st.subheader("1. Bang diem sinh vien")

st.dataframe(

    df.rename(columns={

        "Ho_va_ten": "Ho ten",

        "Chuyen_can": "Chuyen can",

        "Giua_ky": "Giua ky",

        "Cuoi_ky": "Cuoi ky",

        "Tong_ket": "Tong ket",

        "Xep_loai": "Xep loai"

    }).round(2),

    use_container_width=True

)

# Thong ke

st.subheader("2. Thong ke ket qua")

diem_tb = df["Tong_ket"].mean()

cao_nhat = df.loc[df["Tong_ket"].idxmax()]

thap_nhat = df.loc[df["Tong_ket"].idxmin()]

so_dat = int((df["Tong_ket"] >= 5).sum())

c1, c2 = st.columns(2)

c1.metric("Diem trung binh", f"{diem_tb:.2f}")

c2.metric("So sinh vien dat", f"{so_dat}/10")

st.write(

    f"Sinh vien cao nhat: {cao_nhat['Ho_va_ten']} "

    f"({cao_nhat['Tong_ket']:.2f} diem)"

)

st.write(

    f"Sinh vien thap nhat: {thap_nhat['Ho_va_ten']} "

    f"({thap_nhat['Tong_ket']:.2f} diem)"

)

# Chon sinh vien

st.subheader("3. Tra cuu diem sinh vien")

ten = st.selectbox(

    "Chon sinh vien:",

    df["Ho_va_ten"].tolist()

)

sv = df[df["Ho_va_ten"] == ten].iloc[0]

st.write("Ho va ten:", sv["Ho_va_ten"])

st.write("Diem chuyen can:", sv["Chuyen_can"])

st.write("Diem giua ky:", sv["Giua_ky"])

st.write("Diem cuoi ky:", sv["Cuoi_ky"])

st.write("Diem tong ket:", round(sv["Tong_ket"], 2))

st.write("Xep loai:", sv["Xep_loai"])

# Bieu do

st.subheader("4. Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(df["Ho_va_ten"], df["Tong_ket"])

ax.set_title("DIEM TONG KET CUA 10 SINH VIEN")

ax.set_xlabel("Ho ten sinh vien")

ax.set_ylabel("Diem tong ket")

ax.set_ylim(0, 10)

ax.tick_params(axis="x", rotation=45)

fig.tight_layout()

st.pyplot(fig)

# Thong tin nguoi tao

st.caption("Nguoi tao: [Kiều Trần Quang Huy] - MSSV: [052208012120]")
