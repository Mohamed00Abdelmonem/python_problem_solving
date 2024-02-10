def lonelyinteger(arr):
    result = 0
    for num in arr:
        result ^= num  # استخدام XOR لإلغاء تأثير الأرقام المتكررة

    return result


# استدعاء الدالة وطباعة النتيجة
print(lonelyinteger([3,5,2,3,5]))




# def lonelyinteger(arr):
#     # حساب مجموع العناصر المتكررة (مضاعفة)
#     double_sum = sum(set(arr)) * 2
    
#     # حساب مجموع الكل
#     total_sum = sum(arr)
    
#     # الفارق بين مجموع الكل ومجموع العناصر المتكررة يعطي الرقم الفريد
#     unique_number = total_sum - double_sum
    
#     return unique_number


