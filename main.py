from src.chess_tournament.views import Menu

def main():
  menu = Menu()
  
  while True:
    user_choice = menu.choice()
    menu.display(user_choice)
    
    if user_choice == "6":
      break
  
    input("\nAppuyez sur Entrée pour revenir au menu...")  

if __name__ == "__main__":
  main()
  