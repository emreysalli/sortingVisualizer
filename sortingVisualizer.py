from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
from random import shuffle
import time

class animation(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,bg="#001627")
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.pack()
        self.parent.title("Sıralama Algoritmaları Animasyonu")

        frame1=Frame(self.parent,bg="#001627")
        frame1.pack(anchor=W,fill=BOTH)
        L1 = Label(frame1,text="Sıralama Algoritması:",font="Italic 14 bold",fg="#FDFFFD",bg="#001627")
        L1.pack(side=LEFT,anchor=W,padx=50,pady=30)
        self.CB1 = ttk.Combobox(frame1,font="Italic 14 bold",state="readonly",width=20)
        self.CB1.bind("<<ComboboxSelected>>")
        self.CB1.pack(side=LEFT,anchor=W,padx=0,pady=30)
        self.siralamalar=["Bubble Sort","Selection Sort","Insertion Sort","Merge Sort","Quick Sort"]
        self.CB1["values"]=self.siralamalar
        self.B1 = Button(frame1,text="Hazırla",font="Algerian 13 bold",fg="#FDFFFD",bg="#2EC4B6",command=self.create_array)
        self.B1.pack(side=LEFT,anchor=W,padx=200,pady=30)


        frame2=Frame(self.parent,bg="#001627")
        frame2.pack(anchor=W,fill=BOTH)
        L2 =Label(frame2,text="Sayı Adedi:",font="Italic 14 bold",fg="#FDFFFD",bg="#001627")
        L2.pack(side=LEFT,anchor=W,padx=50,pady=0)
        self.var1=StringVar()
        self.E1=Entry(frame2,width=5,font="Italic 14 bold",relief="sunken",bd="4px",textvariable=self.var1)
        self.E1.pack(side=LEFT,anchor=W,padx=0,pady=0)
        L3 = Label(frame2, text="Sayı Aralığı:", font="Italic 14 bold", fg="#FDFFFD", bg="#001627")
        L3.pack(side=LEFT, anchor=W, padx=50, pady=0)
        L4 = Label(frame2, text="0 -", font="Italic 30 bold", fg="#FDFFFD", bg="#001627")
        L4.pack(side=LEFT, anchor=W, padx=0, pady=0)
        self.var2 = StringVar()
        self.E3 = Entry(frame2, width=5, font="Italic 14 bold", relief="sunken", bd="4px", textvariable=self.var2)
        self.E3.pack(side=LEFT, anchor=W, padx=20, pady=0)
        self.B2 = Button(frame2, text="Başlat", font="Algerian 13 bold", fg="#FDFFFD", bg="#2EC4B6",command=self.start)
        self.B2.pack(side=LEFT, anchor=W, padx=150, pady=0)

        frame3 = Frame(self.parent, bg="black")
        frame3.pack(anchor=W, fill=BOTH)
        self.canvas = Canvas(frame3, height=550, width=1000, bg="#FDFFFD")
        self.canvas.pack(side=LEFT, anchor=W, padx=20, pady=20)


    def create_array(self):
        try:
            size = int(self.var1.get())
        except:
            size = 20
        try:
            maxvalue = int(self.var2.get())
        except:
            maxvalue = 20
        self.array = []
        for i in range(0, size):
            self.array.append(random.randint(0, maxvalue))
        self.show(self.array,['#E71D36' for x in range(len(self.array))])


    def show(self,array, array_renk):
        self.canvas.delete(ALL)
        canvas_height=500
        canvas_width=1000
        x_width=canvas_width/(len(self.array)+1)
        array_oran = []
        for i in self.array:
            array_oran.append(i/max(self.array))
        for sira, oran in enumerate(array_oran):
            x0 = sira * x_width
            y0 = canvas_height - oran * 420
            x1 = (sira + 1) * x_width
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=array_renk[sira])

        Frame.update_idletasks(self)

    def start(self):
        try:
            if (self.CB1.get() == "Bubble Sort"):
                self.bubbleSort(self.array)
            elif (self.CB1.get() == "Selection Sort"):
                self.selectionSort(self.array)
            elif (self.CB1.get() == "Insertion Sort"):
                self.insertionSort(self.array)
            elif (self.CB1.get() == "Merge Sort"):
                self.merge_sort(self.array)
            else:
                self.quick_sort(self.array)
        except:
            messagebox.showerror(title="Hata", message="Lütfen ilk önce hazırlayınız!")
    def bubbleSort(self,A):
        n = len(A)

        for i in range(n - 1, 0, -1):
            swapped = False
            for j in range(i):
                # compare the adjacent elements.​
                if (A[j] > A[j + 1]):
                    # Swap them
                    A[j], A[j + 1] = A[j + 1], A[j]
                    swapped = True
                    self.show(A, ['#FF9F1B' if x == j or x == j + 1 else '#E71D36' for x in range(len(A))])
                    time.sleep(0.5)
        self.show(A, ['#FF9F1B' for x in range(len(A))])

    def selectionSort(self,A):
        n = len(A)

        for i in range(0, n, 1):
            min = i
            for j in range(i + 1, n, 1):
                # compare with each until the end.

                self.show(A,['#FF9F1B' if x == i or x == j else '#E71D36' for x in range(len(A))])
                time.sleep(0.5)
                if (A[j] < A[min]):
                    min = j
            # Exchange the pivot with the minimum.
            A[i], A[min] = A[min], A[i]
        self.show(A, ['#FF9F1B' for x in range(len(A))])

    def insertionSort(self,A):
        n = len(A)

        for i in range(1, n, 1):
            # insert A[i] among A[i-1], A[i-2], A[i-3]
            # into correct position.
            for j in range(i, 0, -1):
                self.show(A, ['#FF9F1B' if x == j - 1 or x == j else '#E71D36' for x in range(len(A))])
                time.sleep(0.5)
                if (A[j] < A[j - 1]):
                    # Swap.
                    A[j], A[j - 1] = A[j - 1], A[j]
                    self.show(A, ['#FF9F1B' if x == j - 1 or x == j else '#E71D36' for x in range(len(A))])
                    time.sleep(0.5)
                else:
                    break
        self.show(A, ['#FF9F1B' for x in range(len(A))])

    def merge(self, a, lo, mid, hi):

        i = lo
        j = mid + 1
        aux = list()            # birleştirme işlemi için ara liste.
        aux.extend(a)     # ara listeyi ilk değerlerle  doldur
        # a[lo..hi] 'yı aux[lo..hi]'ya kopyala
        for k in range(lo, hi + 1, 1):
            aux[k] = a[k]
        # a[lo..hi] üzerinde birleştir.
        for k in range(lo, hi + 1, 1):
            if i > mid:
                a[k] = aux[j]
                j = j + 1
            elif j > hi:
                a[k] = aux[i]
                i = i + 1
            elif aux[j] < aux[i]:
                a[k] = aux[j]
                j = j + 1
            else:
                a[k] = aux[i]
                i = i + 1
        self.show(a, ["#FF9F1B" if x >= lo and x <= hi else "#E71D36" for x in range(len(a))])
        time.sleep(0.5)
    def merge_sort (self, a):
        # Gelen listeyi karıştır
        shuffle(a)
        self.m_sort (a, 0, len(a)-1)
        self.show(a, ['#FF9F1B' for x in range(len(a))])
    # a[lo..hi]'ı sırala
    def m_sort(self, a, lo, hi):
        if hi <= lo :                      # base case
            return
        mid = lo + (hi - lo) //2
        self.m_sort(a, lo,  mid)             # sol yarıyı sırala
        self.m_sort(a, mid+1, hi)            # sağ yarıyı sırala
        self.merge(a, lo, mid, hi)         # sonuçları birleştir.


    # Diziyi a[lo..j-1], a[j], a[j+1..hi] olmak üzere iki parçaya böler
    def partition(self, a, lo, hi):
        i, j = lo, hi + 1  # sol ve sağ tarama indisleri
        pivot = a[lo]  # parçalama elemanı
        while (True):
            i = i + 1
            j = j - 1
            while a[i] < pivot:  # soldan sağa doğru pivottan daha büyük buluncaya kadar tara
                if i == hi:
                    break
                i = i + 1
            while pivot < a[j]:  # sağdan sola doğru pivottan daha küçük buluncaya kadar tara
                if j == lo:
                    break
                j = j - 1
            if i >= j:               # Eğer sol ve sağ işaretçiler çakıştıysa bitir.
                break

            a[i], a[j] = a[j], a[i]  # Durduğun gözlerdeki elemanları yer değiştir.
            self.show(a, ['#FF9F1B' if x == i or x == j else '#E71D36' for x in range(len(a))])
            time.sleep(0.5)


        a[lo], a[j] = a[j], a[lo]  # a[lo] ile a[j]'yi yer değiştir.
        self.show(a, ['#FF9F1B' if x == lo or x == j else '#E71D36' for x in range(len(a))])
        time.sleep(0.5)
        return j                     # j'yi geri döndür.

    def quick_sort (self, a):
        random.shuffle(a)               # listeyi karıştırma adımı önemli
        self.q_sort (a, 0, len(a)-1)
        self.show(a, ['#FF9F1B' for x in range(len(a))])

    def q_sort(self, a, lo, hi):
        if hi <= lo :                           # base case
            return
        j = self.partition (a, lo, hi)        # dizi iki parçaya ayrılır.
        self.q_sort(a, lo,  j-1)                     # sol yarıyı sırala
        self.q_sort(a, j+1, hi)                     # sağ yarıyı sırala

def main():
    root=Tk()
    root.geometry("1050x710+0+0")
    app=animation(root)
    root.mainloop()
if __name__=="__main__":
    main()