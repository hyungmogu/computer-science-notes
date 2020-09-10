if [ $# -ne 2 ]
then
    echo usage: arg_number_check_example.sh x y >& 2
    exit 1
fi

expr $1 + $2