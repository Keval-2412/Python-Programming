def remove_string(main_str, remove_string):
   i=0
   result = ""
   found = False
   while i < len(main_str):
      j = 0
      k = i
      while j < len(remove_string) and k < len(main_str) and main_str[k] == remove_string[j]:
         j += 1
         k += 1

         if j == len(remove_string) and not found:
            i = k
            found = True
      else:
         result += main_str[i]
         i += 1
   return result
s1 = "abcdef"
s2 = "cd"
final_string = remove_string(s1,s2)
print("Final string:", final_string)