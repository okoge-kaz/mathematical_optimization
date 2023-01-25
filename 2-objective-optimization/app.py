import matplotlib.pyplot as plt  # type: ignore
import numpy as np


def f_1(x: np.ndarray) -> np.float64:
    # x_1 ^ 2 - x_1 * x_2 + x_2 ^ 2 - x_1 - x_2 + 1
    return x[0] ** 2 - x[0] * x[1] + x[1] ** 2 - x[0] - x[1] + 1


def f_2(x: np.ndarray) -> np.float64:
    # x_1 ^ 2 + x_1 * x_2 + x_2 ^ 2 + 2 * x_1 + 4 * x_2 + 4
    return x[0] ** 2 + x[0] * x[1] + x[1] ** 2 + 2 * x[0] + 4 * x[1] + 4


def f(x: np.ndarray) -> np.float64:
    return np.minimum(f_1(x), f_2(x))


def f_1_gradient(x: np.ndarray) -> np.ndarray:
    # [2 * x_1 - x_2 - 1, -x_1 + 2 * x_2 - 1]
    return np.array([2 * x[0] - x[1] - 1, -x[0] + 2 * x[1] - 1])


def f_2_gradient(x: np.ndarray) -> np.ndarray:
    # [2 * x_1 + x_2 + 2, x_1 + 2 * x_2 + 4]
    return np.array([2 * x[0] + x[1] + 2, x[0] + 2 * x[1] + 4])


def f_gradient(x: np.ndarray) -> np.ndarray:
    return np.minimum(f_1_gradient(x), f_2_gradient(x))


def f_1_hessian(x: np.ndarray) -> np.ndarray:
    # [[2, -1], [-1, 2]]
    return np.array([[2, -1], [-1, 2]])


def f_2_hessian(x: np.ndarray) -> np.ndarray:
    # [[2, 1], [1, 2]]
    return np.array([[2, 1], [1, 2]])


def liner_weight_sum(x: np.ndarray, w_1: np.float64) -> np.float64:
    w2: np.float64 = 1 - w_1
    return w_1 * f_1(x) + w2 * f_2(x)


def liner_weight_sum_gradient(x: np.ndarray, w_1: np.float64) -> np.ndarray:
    w2: np.float64 = 1 - w_1
    return w_1 * f_1_gradient(x) + w2 * f_2_gradient(x)


def newton_method(x: np.ndarray, w_1: np.float64) -> np.ndarray:
    w2: np.float64 = 1 - w_1

    while True:
        hessian: np.ndarray = w_1 * f_1_hessian(x) + w2 * f_2_hessian(x)  # matrix: 2x2
        gradient: np.ndarray = w_1 * f_1_gradient(x) + w2 * f_2_gradient(x)  # vector: 2x1
        x_new = x - np.linalg.inv(hessian) @ gradient  # [2x2] @ [2x1] = [2x1]
        if np.linalg.norm(liner_weight_sum_gradient(x_new, w_1)) < 1e-3:
            return x_new
        x = x_new
        print("x: ", x)
        print("liner_weight_sum_gradient: ", liner_weight_sum_gradient(x, w_1))


def main() -> None:
    ws: np.ndarray = np.linspace(0, 1, 101)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    for w in ws:
        x: np.ndarray = np.array([0, 0])
        x = newton_method(x, w)
        # plot [x[0], x[1]] point on graph for each w
        ax1.scatter(x[0], x[1], c="lightblue")
        # plot [f_1(x), f_2(x)] point on graph for each w
        ax2.scatter(f_1(x), f_2(x), c="lightgreen")

    ax1.set_xlabel("x_1")
    ax1.set_ylabel("x_2")

    ax2.set_xlabel("f_1")
    ax2.set_ylabel("f_2")
    plt.show()


if __name__ == "__main__":
    main()
