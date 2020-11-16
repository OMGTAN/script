from sklearn.linear_model import LinearRegression

X = [[1,1,1],[1,1,2],[1,2,1]]
y = [[6],[9],[8]]

model = LinearRegression()
model.fit(X, y)
x2 = [[1,3,5]]
y2 = model.predict(x2)
print (y2)