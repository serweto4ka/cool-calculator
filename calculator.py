import customtkinter as ctk
import ast
import operator
from typing import Any, Dict, Type


class SafeCalculator:

    def __init__(self):
        self._OPERATORS: Dict[Type[ast.AST], Any] = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.USub: operator.neg, 
        }

    def _safe_eval(self, node: ast.AST) -> float | int:
        
        if isinstance(node, ast.Constant):
            return node.value
        
        elif isinstance(node, ast.Num):
            return node.n

        elif isinstance(node, ast.BinOp):
            op = self._OPERATORS.get(type(node.op))
            if op is None:
                raise TypeError(f"Недозволена операція: {type(node.op)}")
            
            left_val = self._safe_eval(node.left)
            right_val = self._safe_eval(node.right)
            return op(left_val, right_val)
        
        elif isinstance(node, ast.UnaryOp):
            op = self._OPERATORS.get(type(node.op))
            if op is None:
                raise TypeError(f"Недозволена операція: {type(node.op)}")
                
            operand_val = self._safe_eval(node.operand)
            return op(operand_val)
            
        else:
            raise TypeError(f"Недозволений вузол: {type(node)}")

    def calculate(self, expression: str) -> str:
        """Публічний метод для обчислення рядка."""
        if not expression:
            return ""
        try:
            node = ast.parse(expression, mode='eval')
            result = self._safe_eval(node.body)
            if isinstance(result, float) and result.is_integer():
                return str(int(result))
            return str(result)
        
        except (SyntaxError, TypeError, ZeroDivisionError, Exception) as e:
            print(f"Error: {e}")
            return "Помилка"


class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Калькулятор")
        self.geometry("380x540")
        self.resizable(False, False)
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.calculator = SafeCalculator()
        self.display_var = ctk.StringVar()
        
        self._create_widgets()
        
    def _create_widgets(self):
        self.grid_columnconfigure(tuple(range(4)), weight=1)
        self.grid_rowconfigure(tuple(range(6)), weight=1)
        
        display_font = ctk.CTkFont(family="Arial", size=48)
        self.display_entry = ctk.CTkEntry(
            self,
            textvariable=self.display_var,
            font=display_font,
            justify="right",
            corner_radius=10,
            border_width=2,
            fg_color="#2B2B2B",
            state="readonly"
        )
        self.display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew", ipady=20)
        
        button_font = ctk.CTkFont(family="Arial", size=24, weight="bold")
        
        buttons_layout = [
            ('C', 1, 0, "#D65A5A", "#B04A4A"),   
            ('(', 1, 1, "#4A4A4A", "#3A3A3A"),   
            (')', 1, 2, "#4A4A4A", "#3A3A3A"),
            ('<-', 1, 3, "#D65A5A", "#B04A4A"),  
            ('7', 2, 0),
            ('8', 2, 1),
            ('9', 2, 2),
            ('/', 2, 3, "#FF9500", "#D97E00"),   
            ('4', 3, 0),
            ('5', 3, 1),
            ('6', 3, 2),
            ('*', 3, 3, "#FF9500", "#D97E00"),
            ('1', 4, 0),
            ('2', 4, 1),
            ('3', 4, 2),
            ('-', 4, 3, "#FF9500", "#D97E00"),
            ('0', 5, 0),
            ('.', 5, 1),
            ('=', 5, 2, "#34C759", "#2A9E48"),   
            ('+', 5, 3, "#FF9500", "#D97E00"),
        ]
        
        for btn_data in buttons_layout:
            text = btn_data[0]
            row = btn_data[1]
            col = btn_data[2]
            
            fg_color = btn_data[3] if len(btn_data) > 3 else "#6B6B6B"
            hover_color = btn_data[4] if len(btn_data) > 4 else "#5A5A5A"
            
            if text == '0':
                col_span = 1
            else:
                col_span = 1
                
            if text == '=':
                col_span = 2
                
            button = ctk.CTkButton(
                self,
                text=text,
                font=button_font,
                corner_radius=10,
                fg_color=fg_color,
                hover_color=hover_color,
                command=lambda t=text: self._on_button_click(t)
            )
            
            if text == '0':
                button.grid(row=row, column=col, columnspan=1, padx=5, pady=5, sticky="nsew")
            elif text == '=':
                button.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
            else:
                button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5, sticky="nsew")

    def _on_button_click(self, caption: str):
        current_text = self.display_var.get()
        
        if current_text == "Помилка":
            current_text = ""

        if caption == 'C':
            self.display_var.set("")
        elif caption == '<-':
            self.display_var.set(current_text[:-1])
        elif caption == '=':
            result = self.calculator.calculate(current_text)
            self.display_var.set(result)
        else:
            self.display_var.set(current_text + caption)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()