from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches

import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols

def main():


    with PdfPages(r'reg.pdf') as export_pdf:
        Prestige = sm.datasets.get_rdataset("Prestige","carData").data
        txt = "Russell Frith \n Regression Analysis \n"
        txt += "Please give attribution to Russell Frith \n"
        txt += "=========================================\n"
        txt += "Perform a regression analysis on structured data. \n"
        txt += "Predict a target variable from a number of predictor variables. \n"
        txt += "==========================================\n"
        txt += "Use the Prestige.carData data set imported from statsmodels. \n"

        txt += "Dataframe Shape: \n" + str(Prestige.shape) + "\n"
        txt += "Dataframe Columns: \n" + str(Prestige.columns) + "\n"
        txt += "Data types: \n" + str(Prestige.dtypes) + "\n"
        txt += "Dataframe Head: \n" + str(Prestige.head()) + "\n"
        left, width = .25, .5
        bottom, height = .25, .5
        right = left + width
        top = bottom + height

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])

        p = patches.Rectangle(
            (left, bottom), width, height,
            fill=False, transform=ax.transAxes, clip_on=False
        )
        # ax.add_patch(p)

        ax.text(0.5 * (left + right), 0.5 * (bottom + top), txt,
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=8, color='red',
                transform=ax.transAxes)

        ax.set_axis_off()
        export_pdf.savefig()
        plt.close()




        print(Prestige.dtypes)
        print(Prestige.head())
        Prestige['prestige'].describe()
        Prestige['prestige'].hist()
        Prestige['type'].value_counts().plot(kind='bar')
        export_pdf.savefig()
        plt.close()

        Prestige.plot.scatter(x='prestige',y='women')
        print(Prestige.corr())
        export_pdf.savefig()
        plt.close()

        sns.pairplot(Prestige,vars=["education","income","women"])
        #plt.show()
        export_pdf.savefig()
        plt.close()




        est = ols(formula = 'prestige ~ education + income + women + type', data = Prestige).fit()
        #print(est.summary())

        left, width = .25, .5
        bottom, height = .25, .5
        right = left + width
        top = bottom + height

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])

        p = patches.Rectangle(
            (left, bottom), width, height,
            fill=False, transform=ax.transAxes, clip_on=False
        )
        # ax.add_patch(p)

        ax.text(0.5 * (left + right), 0.5 * (bottom + top), est.summary(),
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=8, color='green',
                transform=ax.transAxes)

        ax.set_axis_off()
        export_pdf.savefig()
        plt.close()

if __name__ == '__main__':
    main()
