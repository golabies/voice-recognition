import read_data
import signal_fft
import filters

if __name__ == '__main__':
    data = read_data.ReadData()
    data.read_wave()
    new_signal, fs = data.output()
    fill = filters.Filters(new_signal[0])
    new_signal = fill.smooth(149)
    data.show()
    MF = signal_fft.MyFt(new_signal, fs)
    MF.my_ft()
    MF.show()
