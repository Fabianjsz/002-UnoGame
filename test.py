import tkinter as tk

class TurnGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Turn-Based Game")

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        self.status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 16))
        self.status_label.pack(pady=10)

        self.board_frame = tk.Frame(root)
        self.board_frame.pack()

        for i in range(9):
            btn = tk.Button(self.board_frame, text="", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} wins!")
                self.disable_all()
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        b = self.board
        lines = [
            (0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # columns
            (0,4,8), (2,4,6)            # diagonals
        ]
        for i, j, k in lines:
            if b[i] == b[j] == b[k] != "":
                return True
        return False

    def disable_all(self):
        for btn in self.buttons:
            btn.config(state="disabled")

# Run the game
root = tk.Tk()
game = TurnGame(root)
root.mainloop()
