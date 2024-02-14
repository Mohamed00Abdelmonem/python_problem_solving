# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k

# هدخل نص يرجع ليا نص مشفر عشان محدش يفهمه يعني زود علي كل حرف رقمين كدا يعني
# 
# المسألة تتحدث عن تشفير النصوص باستخدام تقنية تسمى "سيزار سيفر". في هذه التقنية، يتم تحويل كل حرف في النص إلى حرف آخر بناءً على تحول محدد (عدد معين) في الأبجدية.

# مثال:

# لنفترض أن لدينا تحول بمقدار 3، سنقوم بتحويل كل حرف في النص بمقدار 3 حروف لليمين. على سبيل المثال، حرف "a" سيتحول إلى "d"، "b" إلى "e"، وهكذا. إذا وصلنا إلى نهاية الأبجدية، سنعود إلى بدايتها.

# في المسألة، يعطى لك نص غير مشفر وعدد يحدد كم يجب أن يتم تحويل الأبجدية. عليك تطبيق هذا التحويل وإرجاع النص المشفر.

# مثال محدد من المسألة:

# نص غير مشفر: middle-Outz
# تحويل الأبجدية: 2
# النتيجة المشفرة: okffng-Qwvb

# التفاصيل:

# الحرف "m" يتحول بمقدار 2 إلى "o".
# الحرف "i" يتحول بمقدار 2 إلى "k".
# الحرف "d" يتحول بمقدار 2 إلى "f".
# الحرف "l" يتحول بمقدار 2 إلى "n".
# وهكذا...


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesarCipher(s, k):
    # Write your code here
    # alphabet = list("abcdefghijklmnopqrstuvwxyz")
    # new_s = ""
    
    # for x in s:
    #     y = x.lower()
          
    #     if y.isalpha():
    #         index = alphabet.index(y)
    #         y = alphabet[(index+k) % 26]
            
    #     if x.isupper():
    #         y = y.upper()
    #     new_s += y   
        
    # return new_s



    # new_s = ''.join([
    #     alphabet[(alphabet.index(x.lower()) + k) % 26].upper() if x.isalpha() else x
    #     for x in s
    # ])
    # return new_s



    return ''.join([ alphabet[(alphabet.index(char)+k) % 26] if char in s else 'a' if char == 'z' else char for char in s  ])

print(caesarCipher('amdzeo', 2))