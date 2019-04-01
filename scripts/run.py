import scripts.read_data
import scripts.signal_fft
import scripts.filters

if __name__ == '__main__':
    data = scripts.read_data.ReadData()
    data.recording()
    # data.read_wave()
    # data.play()
    data.show()
    # data.save_data()
    new_signal, fs = data.output()
    fill = scripts.filters.Filters(new_signal[0])
    # new_signal = fill.smooth(149)
    # fill.show(fill.smooth, 149)
    MF = scripts.signal_fft.MyFt(new_signal[0], fs)
    MF.my_ft()
    MF.show()
