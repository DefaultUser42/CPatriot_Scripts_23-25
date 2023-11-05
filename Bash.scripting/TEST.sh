read -p "Press any key to continue"
echo finished

echo "Would you like to continue? The following commands are kind of experimental and we could lost points because of them. (y or n)"
read continue
while [ $continue == "n" ]; do
    echo "Finished"
    exit
    break
done

# 

