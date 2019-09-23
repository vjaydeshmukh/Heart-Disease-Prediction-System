def get_history(chol, pressure, max_rate, date):
    import matplotlib
    matplotlib.use('Agg')
    import pandas as pd
    from matplotlib import pyplot as plt
    import os
    from django.conf import settings

    # serum choloestrol
    df = pd.DataFrame(data={"date": date, "att_val": chol})
    df.to_csv("chol.csv", sep=',', index=False)

    df = pd.read_csv('chol.csv', parse_dates=True, index_col='date', sep=",")
    df.plot(color='blue', marker='o', linestyle='dashed', linewidth=0.8, markersize=3)
    plt.title("Serum Cholesterol Data")
    plt.ylabel("Values")
    plt.xlabel("Dates")
    plt.legend(["chol"])
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/graph/chol.png'))
    plt.close()

    # blood pressure
    df = pd.DataFrame(data={"date": date, "att_val": pressure})
    df.to_csv("pressure.csv", sep=',', index=False)

    df = pd.read_csv('pressure.csv', parse_dates=True, index_col='date', sep=",")
    df.plot(color='blue', marker='o', linestyle='dashed', linewidth=0.8, markersize=3)
    plt.title("Blood Pressure Data")
    plt.ylabel("Values")
    plt.xlabel("Dates")
    plt.legend(["bp"])
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/graph/press.png'))
    plt.close()

    # maximum heart rate
    df = pd.DataFrame(data={"date": date, "att_val": max_rate})
    df.to_csv("max_rate.csv", sep=',', index=False)

    df = pd.read_csv('max_rate.csv', parse_dates=True, index_col='date', sep=",")
    df.plot(color='blue', marker='o', linestyle='dashed', linewidth=0.8, markersize=3)
    plt.title("Maximun Heart Rate Achieved")
    plt.ylabel("Values")
    plt.xlabel("Dates")
    plt.legend(["heart-rate"])
    plt.savefig(os.path.join(settings.BASE_DIR, 'static\graph\h_rate.png'))
    plt.close()