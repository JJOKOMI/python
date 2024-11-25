from entity.user_entity import User
from src.repository.user_repository import UserRepositoryStudy


def main():
  # newUser = User(username='dfdf', password='1234', name='황현지', email='dsa@example.com')
  userRepository = UserRepositoryStudy()
  # userRepository.insert(newUser)
  userRepository.findById(1)

if __name__ == "__main__":
  main()