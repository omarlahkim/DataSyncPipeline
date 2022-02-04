from DataEngine import DataEngine
from DatabaseEngine import DatabaseEngine




def main():
    Data_Engine = DataEngine()
    Database_Engine = DatabaseEngine()
    Data_Engine.init_connection()
    Passwd = Data_Engine.read(Data_Engine.getPasswdClient(), 'passwd')
    Shadow = Data_Engine.read(Data_Engine.getShadowClient(), 'shadow')
    da = Data_Engine.join(Passwd, Shadow)
    if Data_Engine.checkFilesChange():
        Database_Engine.truncateTable()
        for i in range(len(da)):
            data = da[i]
            Database_Engine.insertData(data[2], data[0], data[1], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11],data[12], data[3])

    Data_Engine.saveFile(Data_Engine.getShadowClient(), "shadow")
    Data_Engine.saveFile(Data_Engine.getPasswdClient(), "passwd")

if __name__ == "__main__":
    main()