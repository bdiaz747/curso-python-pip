import matplotlib.pyplot as plt

def gererate_pie_chart():
    label = ['A','B','C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels = label)
    plt.savefig('pie.png')
    plt.close()