echo 'p1' > reports/report.txt
python3 p1.py < test.txt > python.txt
./p1 < test.txt > buro.txt
diff python.txt buro.txt >> reports/report.txt
rm buro.txt
rm python.txt

echo 'p2' >> reports/report.txt
python3 p2.py < test2.txt >python.txt
./p2 < test2.txt > buro.txt
diff python.txt buro.txt >> reports/report.txt
rm buro.txt
rm python.txt

echo 'horz' >> reports/report.txt
python3 p2.py < horztest.txt >python.txt
./p2 < horztest.txt > buro.txt
diff python.txt buro.txt >> reports/report.txt
rm buro.txt
rm python.txt

echo 'vert' >> reports/report.txt
python3 p2.py < verttest.txt > python.txt
./p2 < verttest.txt > buro.txt
diff python.txt buro.txt >> reports/report.txt
rm buro.txt
rm python.txt

echo 'full' >> reports/report.txt
python3 p2.py < fulltest.txt > python.txt
./p2 < fulltest.txt > buro.txt
diff python.txt buro.txt >> reports/report.txt
rm buro.txt
rm python.txt

python3 p3.py < test3.txt


