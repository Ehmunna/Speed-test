## Run in Termux 

```python
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git
pip install speedtest-cli requests rich
pkg install sox
git clone https://github.com/Ehmunna/Speed-test.git
cd Speed-test
python test.py
