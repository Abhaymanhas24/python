# class teacher:
#     def english(self):
#         print("English Language")
# class student1(teacher):
#     def language(self):
#         print("english teacher should")
# class student2(teacher):
#     def language(self):
#         print("english teacher should")

# obj1=student1()
# obj2=student2()

# obj1.english()
# obj1.language()


class Father:
    def gender(self):
        print("male")


class Mother:
    def gender(self):
        print("Female")


class child(Father, Mother):
    def gender(self):
        print("male")


obj1 = child()
obj1.gender()
