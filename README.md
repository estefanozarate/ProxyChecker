# Proxy Checker

![network weights](https://raw.github.com/estefanozarate/ProxyChecker/main/running_proxy_checker.png?rar=true)



This is a simple Python script to check the availability of a list of proxies. It utilizes threads for more efficient checking.

## Usage

1. Make sure you have Python installed on your system.
2. Install the required dependencies using the following command:
   ```
   pip install requests termcolor
   ```
3. Place your list of proxies in a text file named `proxy_list_100.txt`, where each line contains a proxy address in the format `address:port`.
4. Run the script using the following command:
   ```
   python proxy_checker.py
   ```

## Operation

The script will perform the following actions:

- Load the list of proxies from the `proxy_list_100.txt` file.
- Check the availability of proxies using threads for faster execution.
- Display the proxies that are working and those that are not.
- Save the results in separate text files (`up_proxy.txt` for working proxies and `down_proxy.txt` for non-working proxies).

## Author
By WildFire
This project was created by https://github.com/estefanozarate