a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
# 아무것도 출력되지 않음

elif "python" in a and "you" not in a:
    print("python")
# 아무것도 출력되지 않음

elif "shirt" not in a:
    print("shirt")
# 'shirt' 출력됨

elif "need" in a:
    print("need")
# 출력되지 않음

else:
    print("none")
# 출력되지 않음
