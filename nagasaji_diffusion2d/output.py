def create_plot(fig, fig_counter, u, n, dt, T_cold, T_hot):
    """
    Create one plot for one time stamp. In diffusion2d.py, there are four plots.
    """
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap='hot', vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return im

def output_plots(fig, im):
    """
    Output all the four plots as one figure.
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
