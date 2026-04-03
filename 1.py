import sympy as sp
x=sp.symbols('x')
f=sp.sin(x)*sp.log(sp.sin(x))
result=sp.integrate(f,(x,0,sp.pi/2))
print(f"该定积分的精确结果为：{result}")
print(f"数值近似值为：{result.evalf()}")