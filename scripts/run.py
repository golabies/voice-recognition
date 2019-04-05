import scripts.read_data
import scripts.signal_fft
import scripts.filters
import scripts.cluster

if __name__ == '__main__':
    data = scripts.read_data.ReadData()
    # data.recording()
    data.read_wave()
    # data.play()
    # data.show()
    # data.save_data()
    new_signal, fs = data.output()
    fill = scripts.filters.Filters()
    new_signal = fill.smooth(new_signal[0], 149)
    # fill.show(fill.smooth, 149)
    new_signal_1 = fill.differences(new_signal)
    fill.show(fill.differences, new_signal)
    # cls = scripts.cluster.Cluster(new_signal_1)
    # cls.clustering()
    # cls.show()
    MF = scripts.signal_fft.MyFt(new_signal_1, fs)
    MF.my_ft()
    MF.show()
    show_text = speech_to_text.to_text()
    show_text.print_text()
    print(show_text.out_put())
