import streamlit as st

def calculator():
    st.title("計算機")

    # ユーザーに数値を入力してもらう
    num1 = st.number_input("最初の数字を入力してください:", value=0.0)
    num2 = st.number_input("二つ目の数字を入力してください:", value=0.0)

    # ユーザーが計算する操作を選択
    operation = st.radio("Select operation:", options=["足し算", "引き算", "掛け算", "割り算"])

    # 計算ボタンが押されたら結果を表示
    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.success(f"計算結果は {operation} {num1} and {num2} で: {result}")

def calculate(num1, num2, operation):
    if operation == "足し算":
        return num1 + num2
    elif operation == "引き算":
        return num1 - num2
    elif operation == "掛け算":
        return num1 * num2
    elif operation == "割り算":
        if num2 != 0:
            return num1 / num2
        else:
            st.error("Cannot divide by zero.")
            return None

# アプリケーションの実行
if __name__ == "__main__":
    calculator()
