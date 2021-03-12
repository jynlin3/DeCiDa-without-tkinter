from decida.Data import Data
import numpy as np
Iin_avg_array=[]
stop_vo_array=[]
final_vo_array=[]
tend = 550e-6
for i in range(1):
    input_file = "tb.tr" + str(i)
    d = Data()
    d.read_hspice(input_file)
    #d.names()
    time=d.get('TIME')
    vout=d.get('v(vout))')
    Iin=d.get('i(vvin))')
    stop_recycle=d.get('v(stop_recycle))')
    zcd=d.get('v(zcd))')
    Iin_avg = np.sum((time[1:] - time[:-1]) * (Iin[1:] + Iin[:-1]) / 2) / tend
    Iin_avg_array.append(Iin_avg)
    for j in range(len(time)):
        if time[j] > 1e-6 and stop_recycle[j] > 0.6 and zcd[j] >0.6:
            stop_vo_array.append(vout[j])
            break
    final_vo_array.append(vout[-1])
output_filename="extracted_result.txt"
with open(output_filename, "w") as f:
    f.write("Iin_avg\tstop_vo\tfinal_vo\n")
    for i in range(len(Iin_avg_array)):
        f.write("%e\t%f\t%f\n" %(Iin_avg_array[i], stop_vo_array[i], final_vo_array[i]))

f.close()
print('time=%e' %(time[-1]))
print('vout=%e' %(vout[-1]))
print(Iin_avg)

