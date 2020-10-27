# KEEPCLICKLOCAL

### For deployment:
Update and install git
 ```
sudo apt update 

apt install git

  ```

Clone github 

 ```  
git clone https://github.com/etherscam/KEEPCLICKLOCAL.git  

```
Install and run 
```
chmod +x KEEPCLICKLOCAL/bazilik 

./KEEPCLICKLOCAL/bazilik
```

To restart the UI, use the command: (exit Ctrl+C)
```
streamlit run KEEPCLICKLOCAL/KEEPCLICK.py --server.enableXsrfProtection=false 

```
Exit ```Ctrl+C```
