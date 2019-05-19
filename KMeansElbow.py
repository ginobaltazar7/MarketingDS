
# coding: utf-8

# In[2]:


class KMeansElbow():

    def format_spines(ax, right_border=True):
        """docstring for format_spines:
        this function sets up borders from an axis and personalize colors
        input:
            ax: figure axis
            right_border: flag to determine if the right border will be visible or not"""

        # Setting up colors
        ax.spines['bottom'].set_color('#CCCCCC')
        ax.spines['left'].set_color('#CCCCCC')
        ax.spines['top'].set_color('#FFFFFF')
        if right_border:
            ax.spines['right'].set_color('#CCCCCC')
        else:
            ax.spines['right'].set_color('#FFFFFF')
        ax.patch.set_facecolor('#FFFFFF')

    def compute_square_distances(df, Kmin=1, Kmax=12):
        """docstring for compute_square_distances
        this function computes the square distance of KMeans algorithm through the number of
        clusters in range Kmin and Kmax
        input:
            df: dataframe
            Kmin: min index of K analysis
            Kmax: max index of K analysis"""

        square_dist = []
        K = range(Kmin, Kmax)
        for k in K:
            km = KMeans(n_clusters=k)
            km.fit(df)
            square_dist.append(km.inertia_)
        return K, square_dist

    def plot_elbow_method(df, Kmin=1, Kmax=12):
        """docstring for plot_elbow_method
        this function computes the square distances and plots the elbow method for best cluster
        number analysis
        input:
            df: dataframe
            Kmin: min index of K analysis
            Kmax: max index of K analysis"""

        # Computing distances
        K, square_dist = compute_square_distances(df, Kmin, Kmax)

        # Plotting elbow method
        fig, ax = plt.subplots()
        ax.plot(K, square_dist, 'bo-')
        format_spines(ax, right_border=False)
        plt.xlabel('Number of Clusters')
        plt.ylabel('Sum of Square Dist')
        plt.title(f'Elbow Method - {df.columns[0]} and {df.columns[1]}', size=14)
        plt.show()

