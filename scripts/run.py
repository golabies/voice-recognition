import scripts.read_data
import scripts.signal_fft
import scripts.filters

if __name__ == '__main__':
    data = scripts.read_data.ReadData()
    data.read_wave()
    new_signal, fs = data.output()
    fill = scripts.filters.Filters(new_signal[0])
    new_signal = fill.smooth(149)
    data.show()
    MF = scripts.signal_fft.MyFt(new_signal, fs)
    MF.my_ft()
    MF.show()
