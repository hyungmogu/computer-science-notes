array=("hello" "goodbye" 2)
for i in "${array[@]}"
do
    case $i in
        hello)
            echo "hello there"
            ;;
        goodbye)
            echo "see you later"
            ;;
        *)
            echo "it's a pleasure to meet you"
            ;;
    esac
done