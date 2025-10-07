import tkinter as tk
from affine_cipher import (
    encrypt,
    decrypt,
    get_filtered_input,
    get_cipher_alphabet,
    check_key_a,
    DEFAULT_ALPHABET,
)

DARK_BG = "#202024"
LIGHT_TXT = "#08AC2C"
DARK_ENTRY = "#252A28"
FONT = ("Consolas, Courier New, Arial", 13)
HEADER_FONT = ("Consolas, Courier New, Arial", 18, "bold")


class AffineCipherGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Affine Cipher")
        self.configure(bg=DARK_BG)
        self.geometry("460x650")
        self.resizable(False, False)
        self.create_widgets()

    def label(self, text, x, y, font=FONT, anchor="w"):
        return tk.Label(
            self, text=text, bg=DARK_BG, fg=LIGHT_TXT, font=font, anchor=anchor
        ).place(x=x, y=y)

    def entry(self, width, x, y, default="", state=tk.NORMAL):
        e = tk.Entry(
            self,
            width=width,
            font=FONT,
            bg=DARK_ENTRY,
            fg=LIGHT_TXT,
            insertbackground=LIGHT_TXT,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground=LIGHT_TXT,
            selectbackground=LIGHT_TXT,
            selectforeground=DARK_BG,
        )
        e.place(x=x, y=y)
        e.insert(0, default)
        e.config(state=state)
        return e

    def text(self, width, height, x, y, state=tk.NORMAL):
        t = tk.Text(
            self,
            width=width,
            height=height,
            font=FONT,
            bg=DARK_ENTRY,
            fg=LIGHT_TXT,
            insertbackground=LIGHT_TXT,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground=LIGHT_TXT,
            selectbackground=LIGHT_TXT,
            selectforeground=DARK_BG,
        )
        t.place(x=x, y=y)
        t.config(state=state)
        return t

    def create_widgets(self):
        self.label("Key A", 45, 20)
        self.label("Key B", 260, 20)
        self.key_a = self.entry(8, 50, 50, "5")
        self.key_a.bind("<KeyRelease>", lambda e: self.update_all())
        self.key_b = self.entry(8, 265, 50, "8")
        self.key_b.bind("<KeyRelease>", lambda e: self.update_all())

        self.label("ENTER TEXT", 45, 95)
        self.input_text = self.text(32, 4, 50, 125)
        self.input_text.bind("<KeyRelease>", lambda e: self.update_all())

        self.label("OUTPUT", 45, 220)
        self.output_text = self.text(32, 4, 50, 250, state=tk.DISABLED)

        self.encrypt_btn = tk.Button(
            self,
            text="ENCRYPT",
            font=FONT,
            width=7,
            bg=DARK_ENTRY,
            fg=LIGHT_TXT,
            activebackground=DARK_BG,
            activeforeground=DARK_BG,
            borderwidth=0,
            command=self.do_encrypt,
            state=tk.DISABLED,
        )
        self.encrypt_btn.place(x=50, y=345)

        self.clear_btn = tk.Button(
            self,
            text="CLEAR",
            font=FONT,
            width=7,
            bg=DARK_ENTRY,
            fg=LIGHT_TXT,
            activebackground=DARK_BG,
            activeforeground=DARK_BG,
            borderwidth=0,
            command=self.clear_fields,
        )
        self.clear_btn.place(x=297, y=345)

        self.decrypt_btn = tk.Button(
            self,
            text="DECRYPT",
            font=FONT,
            width=7,
            bg=DARK_ENTRY,
            fg=LIGHT_TXT,
            activebackground=DARK_BG,
            activeforeground=DARK_BG,
            borderwidth=0,
            command=self.do_decrypt,
            state=tk.DISABLED,
        )
        self.decrypt_btn.place(x=173, y=345)

        self.info_label = tk.Label(
            self, text="", bg=DARK_BG, fg="red", font=("Consolas", 11), anchor="w"
        )
        self.info_label.place(x=50, y=375)

        self.label("Alphabet:", 45, 400)
        self.alphabet_label = self.text(32, 2, 50, 425, state=tk.DISABLED)

        self.label("Ciphered Alphabet:", 45, 480)
        self.ciphered_alpha_label = self.text(32, 2, 50, 505, state=tk.DISABLED)

        self.label("Filtered Input:", 45, 555)
        self.filtered_label = self.text(32, 1, 50, 580, state=tk.DISABLED)

        self.update_all()

    def update_all(self):
        self.validate_keys()
        self.update_alphabet_labels()

    def update_alphabet_labels(self):
        try:
            alphabet = DEFAULT_ALPHABET
            self.alphabet_label.config(state=tk.NORMAL)
            self.alphabet_label.delete("1.0", tk.END)
            self.alphabet_label.insert(tk.END, alphabet)
            self.alphabet_label.config(state=tk.DISABLED)

            a = int(self.key_a.get())
            b = int(self.key_b.get())
            if check_key_a(a, alphabet):
                ciphered = get_cipher_alphabet(a, b, alphabet)
                self.ciphered_alpha_label.config(state=tk.NORMAL)
                self.ciphered_alpha_label.delete("1.0", tk.END)
                self.ciphered_alpha_label.insert(tk.END, ciphered)
                self.ciphered_alpha_label.config(state=tk.DISABLED)
            else:
                self.ciphered_alpha_label.config(state=tk.NORMAL)
                self.ciphered_alpha_label.delete("1.0", tk.END)
                self.ciphered_alpha_label.insert(tk.END, "INVALID KEY A")
                self.ciphered_alpha_label.config(state=tk.DISABLED)

            plain = self.input_text.get("1.0", "end-1c")
            filtered = get_filtered_input(plain, alphabet)
            self.filtered_label.config(state=tk.NORMAL)
            self.filtered_label.delete("1.0", tk.END)
            self.filtered_label.insert(tk.END, filtered)
            self.filtered_label.config(state=tk.DISABLED)
        except Exception as e:
            self.ciphered_alpha_label.config(state=tk.NORMAL)
            self.ciphered_alpha_label.delete("1.0", tk.END)
            self.ciphered_alpha_label.insert("1.0", "ERROR")
            self.ciphered_alpha_label.config(state=tk.DISABLED)
            self.filtered_label.config(state=tk.NORMAL)
            self.filtered_label.delete("1.0", tk.END)
            self.filtered_label.insert("1.0", "ERROR")
            self.filtered_label.config(state=tk.DISABLED)

    def validate_keys(self):
        try:
            a = int(self.key_a.get())
            b = int(self.key_b.get())
            alphabet = DEFAULT_ALPHABET
            if not (1 <= a < len(alphabet)):
                self.info_label.config(text="Key A out of range!")
                self.encrypt_btn.config(state=tk.DISABLED)
                self.decrypt_btn.config(state=tk.DISABLED)
                return
            if not check_key_a(a, alphabet):
                self.info_label.config(text="Key A not coprime !")
                self.encrypt_btn.config(state=tk.DISABLED)
                self.decrypt_btn.config(state=tk.DISABLED)
                return
            if not (0 <= b < len(alphabet)):
                self.info_label.config(text="Key B out of range!")
                self.encrypt_btn.config(state=tk.DISABLED)
                self.decrypt_btn.config(state=tk.DISABLED)
                return
            self.info_label.config(text="")
            self.encrypt_btn.config(state=tk.NORMAL)
            self.decrypt_btn.config(state=tk.NORMAL)
        except Exception:
            self.info_label.config(text="Keys must be integers!")
            self.encrypt_btn.config(state=tk.DISABLED)
            self.decrypt_btn.config(state=tk.DISABLED)

    def do_encrypt(self):
        plain = self.input_text.get("1.0", "end-1c")
        a = int(self.key_a.get())
        b = int(self.key_b.get())
        alphabet = DEFAULT_ALPHABET
        cipher = encrypt(plain, a, b, alphabet)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, cipher)
        self.output_text.config(state=tk.DISABLED)
        self.update_alphabet_labels()

    def do_decrypt(self):
        cipher = self.input_text.get("1.0", "end-1c")
        a = int(self.key_a.get())
        b = int(self.key_b.get())
        alphabet = DEFAULT_ALPHABET
        try:
            plain = decrypt(cipher, a, b, alphabet)
        except Exception as e:
            plain = f"Error: {e}"
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, plain)
        self.output_text.config(state=tk.DISABLED)
        self.update_alphabet_labels()

    def clear_fields(self):
        self.input_text.config(state=tk.NORMAL)
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.update_alphabet_labels()


if __name__ == "__main__":
    app = AffineCipherGUI()
    app.mainloop()
