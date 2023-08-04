from Manager import Manager
import threading

if __name__ == "__main__":    

    app = Manager()
    
    app.logger.info("Solution Starting ...")

    # threading.Thread(target=app.alerts.check_alerts())

    app.mainloop()
    
    app.logger.info("Solution CLosing ...")