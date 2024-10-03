Hora1Hora=int(input("Dame la primera hora (0-23): "))

if 0<Hora1Hora<23:

    Hora1Minutos=int(input("Dame el primer minuto (0-59): "))

    if 0<Hora1Minutos<59:

        Hora1Segundos=int(input("Dame el primer segundo (0-59): "))

        if 0<Hora1Segundos<59:
           
            Hora2Hora=int(input("Dame la 2ª hora (0-23): "))
            
            if 0<Hora2Hora<23:

                Hora2Minutos=int(input("Dame el 2º minuto (0-59): "))
            
                if 0<Hora2Minutos<59:

                    Hora2Segundos=int(input("Dame el 2º segundo (0-59): "))

                    if 0<Hora2Segundos<59:
                        
                        if Hora1Hora<Hora2Hora:
                            print("Hora 1: %s:%s:%s"%(Hora1Hora,Hora1Minutos,Hora1Segundos))
                            print("Hora 2: %s:%s:%s"%(Hora2Hora,Hora2Minutos,Hora2Segundos))
                            print("La segunda hora es mayor")
                        elif Hora1Hora>Hora2Hora:
                            print("Hora 1: %s:%s:%s"%(Hora1Hora,Hora1Minutos,Hora1Segundos))
                            print("Hora 2: %s:%s:%s"%(Hora2Hora,Hora2Minutos,Hora2Segundos))
                            print("La primera hora es mayor")
                        else:
                            
                            if Hora1Minutos<Hora2Minutos:
                                print("Hora 1: %s:%s:%s"%(Hora1Hora,Hora1Minutos,Hora1Segundos))
                                print("Hora 2: %s:%s:%s"%(Hora2Hora,Hora2Minutos,Hora2Segundos))
                                print("La segunda hora es mayor")
                            elif Hora1Minutos>Hora2Minutos:
                                print("Hora 1: %s:%s:%s"%(Hora1Hora,Hora1Minutos,Hora1Segundos))
                                print("Hora 2: %s:%s:%s"%(Hora2Hora,Hora2Minutos,Hora2Segundos))
                                print("La primera hora es mayor")
                            else:

                                if Hora1Segundos<Hora2Segundos:
                                    print("Hora 1: %s:%s:%s"%(Hora1Hora,Hora1Minutos,Hora1Segundos))
                                    print("Hora 2: %s:%s:%s"%(Hora2Hora,Hora2Minutos,Hora2Segundos))
                                    print("La segunda hora es mayor")
                                elif Hora1Segundos>Hora2Segundos:
                                    print("Hora 1: %s:%s:%s"%(Hora1Hora,Hora1Minutos,Hora1Segundos))
                                    print("Hora 2: %s:%s:%s"%(Hora2Hora,Hora2Minutos,Hora2Segundos))
                                    print("La primera hora es mayor")
                                else:
                                    print("Hora 1: %s:%s:%s"%(Hora1Hora,Hora1Minutos,Hora1Segundos))
                                    print("Hora 2: %s:%s:%s"%(Hora2Hora,Hora2Minutos,Hora2Segundos))
                                    print("LAs dos horas son iguales")

                    else:
                        print("El segundo es invalido")
                else:
                    print("El minuto es invalido")
            else:
                print("La hora es invalida")
        else:
            print("El segundo es invalido")
    else:
        print("El minuto es invalido")
else:
    print("La hora es invalida")