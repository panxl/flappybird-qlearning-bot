for i in `seq -f"%02g" 0 19`; do mv $i/output.dat $i/output_$1.dat; done

for i in `seq -f"%02g" 0 19`; do
    grep Score $i/output_$1.dat | cut -f2 -d" " | awk '{ total += $1 } END { print total/NR }'
done

python mix.py $1

for i in `seq -f"%02g" 0 19`; do
    cp qvalues_$1.json $i/qvalues.json
done
