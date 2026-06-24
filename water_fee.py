import tkinter as tk
from tkinter import messagebox as msg


class water_fee:
    def __init__(
        self,
        root,
    ):
        self.root = root
        self.toelit = tk.IntVar()
        self.first_renter = tk.IntVar()
        self.secend_renter = tk.IntVar()
        self.third_renter = tk.IntVar()
        self.fourth_renter = tk.IntVar()
        self.fifth_renter = tk.IntVar()
        self.tatal_cumsumption = tk.IntVar()
        self.first_renter_money = tk.DoubleVar()
        self.secend_renter_money = tk.DoubleVar()
        self.third_renter_money = tk.DoubleVar()
        self.fourth_renter_money = tk.DoubleVar()
        self.fifth_renter_money = tk.DoubleVar()

        self.label_title1 = tk.Label(root, text="前次抄表日")
        self.label_title1.grid(row=0, column=0)
        self.Entry_date1 = tk.Entry(root, width=10)
        self.Entry_date1.grid(row=0, column=1)
        self.label_title2 = tk.Label(root, text="本次抄表日")
        self.label_title2.grid(row=0, column=2)
        self.Entry_date2 = tk.Entry(root, width=10)
        self.Entry_date2.grid(row=0, column=3)
        self.lable_title3 = tk.Label(root, text="本次水單總費用")
        self.lable_title3.grid(row=0, column=4)
        self.Entry_money = tk.Entry(root, width=10)
        self.Entry_money.grid(row=0, column=5)
        self.Entry_money.insert(0, 0)

        self.label0 = tk.Label(root, text="廁所")
        self.label0.grid(row=1, column=0)

        self.Entry1 = tk.Entry(root, width=10)
        self.Entry1.grid(row=2, column=0)
        self.Entry1.insert(0, "洗車廠")
        self.Entry2 = tk.Entry(root, width=10)
        self.Entry2.grid(row=3, column=0)
        self.Entry2.insert(0, "水果行")
        self.Entry3 = tk.Entry(root, width=10)
        self.Entry3.grid(row=4, column=0)
        self.Entry3.insert(0, "皇億修車廠")
        self.Entry4 = tk.Entry(root, width=10)
        self.Entry4.grid(row=5, column=0)
        self.Entry4.insert(0, "正芳驗車廠")
        self.Entry5 = tk.Entry(root, width=10)
        self.Entry5.grid(row=6, column=0)
        self.Entry5.insert(0, "喬美海產店")

        self.Entry0_1 = tk.Entry(root, width=10)
        self.Entry0_1.grid(row=1, column=1)
        self.Entry0_1.insert(0, 0)
        self.Entry1_1 = tk.Entry(root, width=10)
        self.Entry1_1.grid(row=2, column=1)
        self.Entry1_1.insert(0, 0)
        self.Entry2_1 = tk.Entry(root, width=10)
        self.Entry2_1.grid(row=3, column=1)
        self.Entry2_1.insert(0, 0)
        self.Entry3_1 = tk.Entry(root, width=10)
        self.Entry3_1.grid(row=4, column=1)
        self.Entry3_1.insert(0, 0)
        self.Entry4_1 = tk.Entry(root, width=10)
        self.Entry4_1.grid(row=5, column=1)
        self.Entry4_1.insert(0, 0)
        self.Entry5_1 = tk.Entry(root, width=10)
        self.Entry5_1.grid(row=6, column=1)
        self.Entry5_1.insert(0, 0)
        self.Entry0_2 = tk.Entry(root, width=10)
        self.Entry0_2.grid(row=1, column=3)
        self.Entry0_2.insert(0, 0)
        self.Entry1_2 = tk.Entry(root, width=10)
        self.Entry1_2.grid(row=2, column=3)
        self.Entry1_2.insert(0, 0)
        self.Entry2_2 = tk.Entry(root, width=10)
        self.Entry2_2.grid(row=3, column=3)
        self.Entry2_2.insert(0, 0)
        self.Entry3_2 = tk.Entry(root, width=10)
        self.Entry3_2.grid(row=4, column=3)
        self.Entry3_2.insert(0, 0)
        self.Entry4_2 = tk.Entry(root, width=10)
        self.Entry4_2.grid(row=5, column=3)
        self.Entry4_2.insert(0, 0)
        self.Entry5_2 = tk.Entry(root, width=10)
        self.Entry5_2.grid(row=6, column=3)
        self.Entry5_2.insert(0, 0)

        self.result_Lable1 = tk.Label(root, textvariable=self.first_renter_money)
        self.result_Lable1.grid(row=2, column=4)
        self.result_Lable2 = tk.Label(root, textvariable=self.secend_renter_money)
        self.result_Lable2.grid(row=3, column=4)
        self.result_Lable3 = tk.Label(root, textvariable=self.third_renter_money)
        self.result_Lable3.grid(row=4, column=4)
        self.result_Lable4 = tk.Label(root, textvariable=self.fourth_renter_money)
        self.result_Lable4.grid(row=5, column=4)
        self.result_Lable5 = tk.Label(root, textvariable=self.fifth_renter_money)
        self.result_Lable5.grid(row=6, column=4)

        self.Button1 = tk.Button(
            root, text="資料讀入記憶體", command=lambda: self.consumption_caculate()
        )
        self.Button1.grid(row=7, column=0)

        self.Button2 = tk.Button(
            root, text="水費計算", command=lambda: self.fee_share()
        )
        self.Button2.grid(row=7, column=1)
        self.Button_close = tk.Button(root, text="關閉視窗", command=root.destroy)
        self.Button_close.grid(row=0, column=100)
        self.Button_clear = tk.Button(
            root, text="清除計算", command=lambda: self.clear_caculator()
        )
        self.Button_clear.grid(row=7, column=2)

    def consumption_caculate(self):
        try:

            toelit_before = int(self.Entry0_1.get())
            toelit_after = int(self.Entry0_2.get())
            first_renter_before = int(self.Entry1_1.get())
            first_renter_after = int(self.Entry1_2.get())
            second_renter_before = int(self.Entry2_1.get())
            second_renter_after = int(self.Entry2_2.get())
            thrid_renter_before = int(self.Entry3_1.get())
            thrid_renter_after = int(self.Entry3_2.get())
            fourth_renter_before = int(self.Entry4_1.get())
            fourth_renter_after = int(self.Entry4_2.get())
            fifth_renter_before = int(self.Entry5_1.get())
            fifth_renter_after = int(self.Entry5_2.get())

            toelit = toelit_after - toelit_before
            first_renter = first_renter_after - first_renter_before
            secend_renter = second_renter_after - second_renter_before
            third_renter = thrid_renter_after - thrid_renter_before
            fourth_renter = fourth_renter_after - fourth_renter_before
            fifth_renter = fifth_renter_after - fifth_renter_before

            check0 = False
            check1 = False
            check2 = False
            check3 = False
            check4 = False
            check5 = False
            if toelit <= 0:
                check0 = not msg.askokcancel(message="請確認這次廁所沒水費變動")
            if first_renter <= 0:
                first_renter_name = self.Entry1.get()
                check1 = not msg.askokcancel(
                    message=f"請確認這次{first_renter_name}沒水費變動"
                )
            if secend_renter <= 0:
                secend_renter_name = self.Entry2.get()
                check2 = not msg.askokcancel(
                    message=f"請確認這次{secend_renter_name}廁所沒水費變動"
                )
            if third_renter <= 0:
                third_renter_name = self.Entry3.get()
                check3 = not msg.askokcancel(
                    message=f"請確認這次{third_renter_name}沒水費變動"
                )
            if fourth_renter <= 0:
                fourth_renter_name = self.Entry4.get()
                check4 = not msg.askokcancel(
                    message=f"請確認這次{fourth_renter_name}沒水費變動"
                )
            if fifth_renter <= 0:
                fifth_renter_name = self.Entry5.get()
                check5 = not msg.askokcancel(
                    message=f"請確認這次{fifth_renter_name}沒水費變動"
                )
            totalcheck = check0 | check1 | check2 | check3 | check4 | check5
            if totalcheck:
                raise ValueError("使用者要修正資料，資料未傳入記憶體")
            else:
                total = (
                    toelit
                    + first_renter
                    + secend_renter
                    + third_renter
                    + fourth_renter
                    + fifth_renter
                )
                finalcheck = msg.askyesnocancel(
                    message=f"本月總耗水為{total}度，請核對水費單是否在{total}正負2度內"
                )
                if finalcheck == True:
                    self.toelit.set(toelit)
                    self.first_renter.set(first_renter)
                    self.secend_renter.set(secend_renter)
                    self.third_renter.set(third_renter)
                    self.fourth_renter.set(fourth_renter)
                    self.fifth_renter.set(fifth_renter)
                    self.tatal_cumsumption.set(total)
                    msg.showinfo(message="資料存入記憶體，可計算數值")
                else:
                    msg.showwarning(
                        message="使用者核對資料有異常，暫不存入記憶體(不可進行下一步驟的計算)"
                    )

        except TypeError:
            msg.showerror(message="請輸入阿拉伯數字")
        except Exception as e:
            msg.showerror(message=f"{e}")

    def fee_share(self):
        try:

            total_money = int(self.Entry_money.get())
            toelit = self.toelit.get()
            first_renter = self.first_renter.get()
            secend_renter = self.secend_renter.get()
            third_renter = self.third_renter.get()
            fourth_renter = self.fourth_renter.get()
            fifth_renter = self.fifth_renter.get()
            tatal_cumsumption = self.tatal_cumsumption.get()
            without_toelit_total = tatal_cumsumption - toelit

            first_renter_plus = first_renter + toelit * (
                first_renter / without_toelit_total
            )
            # print(f"第一間度數+上廁所分攤為{first_renter_plus}度")

            secend_renter_plus = secend_renter + toelit * (
                secend_renter / without_toelit_total
            )
            # print(f"第二間度數+上廁所分攤為{secend_renter_plus}度")
            third_renter_plus = third_renter + toelit * (
                third_renter / without_toelit_total
            )
            # print(f"第三間度數+上廁所分攤為{third_renter_plus}度")
            fourth_renter_plus = fourth_renter + toelit * (
                fourth_renter / without_toelit_total
            )
            # print(f"第四間度數+上廁所分攤為{fourth_renter_plus}度")
            fifth_renter_plus = fifth_renter + toelit * (
                fifth_renter / without_toelit_total
            )
            # print(f"第一間度數+上廁所分攤為{fifth_renter_plus}度")

            first_renter_money = round(
                total_money * (first_renter_plus / tatal_cumsumption), 1
            )
            self.first_renter_money.set(first_renter_money)
            # print(f"第一間水費應收{first_renter_money}元")
            secend_renter_money = round(
                total_money * (secend_renter_plus / tatal_cumsumption), 1
            )
            self.secend_renter_money.set(secend_renter_money)
            # print(f"第二間水費應收{secend_renter_money}元")
            third_renter_money = round(
                total_money * (third_renter_plus / tatal_cumsumption), 1
            )
            self.third_renter_money.set(third_renter_money)
            # print(f"第三間水費應收{third_renter_money}元")
            fourth_renter_money = round(
                total_money * (fourth_renter_plus / tatal_cumsumption), 1
            )
            self.fourth_renter_money.set(fourth_renter_money)
            # print(f"第四間水費應收{fourth_renter_money}元")
            fifth_renter_money = round(
                total_money * (fifth_renter_plus / tatal_cumsumption), 1
            )
            self.fifth_renter_money.set(fifth_renter_money)
            # print(f"第五間水費應收{fifth_renter_money}元")

        except Exception as e:
            msg.showerror(message=f"{e}")

    def clear_caculator(self):
        self.toelit.set(0)
        self.first_renter.set(0)
        self.secend_renter.set(0)
        self.third_renter.set(0)
        self.fourth_renter.set(0)
        self.fifth_renter.set(0)
        self.tatal_cumsumption.set(0)
        self.first_renter_money.set(0.0)
        self.secend_renter_money.set(0.0)
        self.third_renter_money.set(0.0)
        self.fourth_renter_money.set(0.0)
        self.fifth_renter_money.set(0.0)

        self.Entry0_1.delete(0, tk.END)
        self.Entry0_1.insert(0, 0)
        self.Entry1_1.delete(0, tk.END)
        self.Entry1_1.insert(0, 0)
        self.Entry2_1.delete(0, tk.END)
        self.Entry2_1.insert(0, 0)
        self.Entry3_1.delete(0, tk.END)
        self.Entry3_1.insert(0, 0)
        self.Entry4_1.delete(0, tk.END)
        self.Entry4_1.insert(0, 0)
        self.Entry5_1.delete(0, tk.END)
        self.Entry5_1.insert(0, 0)
        self.Entry0_2.delete(0, tk.END)
        self.Entry0_2.insert(0, 0)
        self.Entry1_2.delete(0, tk.END)
        self.Entry1_2.insert(0, 0)
        self.Entry2_2.delete(0, tk.END)
        self.Entry2_2.insert(0, 0)
        self.Entry3_2.delete(0, tk.END)
        self.Entry3_2.insert(0, 0)
        self.Entry4_2.delete(0, tk.END)
        self.Entry4_2.insert(0, 0)
        self.Entry5_2.delete(0, tk.END)
        self.Entry5_2.insert(0, 0)
        self.Entry_money.delete(0, tk.END)
        self.Entry_money.insert(0, 0)
        self.Entry_date1.delete(0, tk.END)
        self.Entry_date2.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("鐵皮屋水費計算機")
    root.geometry("600x300")
    water_fee(root)

    root.mainloop()
