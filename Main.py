from Manager import Manager

if __name__ == "__main__":    

    app = Manager()

    app.logger.info("Solution Starting ...")

    app.mainloop()
    
    app.logger.info("Solution CLosing ...")