from sklearn import linear_model

def solve(y, x, x_pred):
    lm = linear_model.LinearRegression()
    lm.fit(x,y)
    y_pred = lm.predict(x_pred)
    return y_pred

m, n = map(int, input().strip().split())
y = []
x = []
x_pred = []

for i in range(n):
    *features, y_val = map(float, input().strip().split())
    x.append(features)
    y.append(y_val)

for i in range(int(input())):
    features = list(map(float, input().strip().split()))
    x_pred.append(features)

answer = solve(y, x, x_pred)
for num in answer:
    print(round(num,2))


