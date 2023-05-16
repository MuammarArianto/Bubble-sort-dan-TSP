import sys


class TravelingSalesmanProblem:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.distance_matrix = [[0] * num_cities for _ in range(num_cities)]
        self.visited = [False] * num_cities
        self.tour = []
        self.total_distance = sys.maxsize

    def add_distance(self, city1, city2, distance):
        self.distance_matrix[city1][city2] = distance
        self.distance_matrix[city2][city1] = distance

    def tsp(self, start_city):
        self.visited[start_city] = True
        self.tour.append(start_city)
        self._tsp_util(start_city, 1, 0)

    def _tsp_util(self, current_city, num_visited, current_distance):
        if num_visited == self.num_cities:
            if self.distance_matrix[current_city][0] != 0:
                total_distance = current_distance + self.distance_matrix[current_city][0]
                if total_distance < self.total_distance:
                    self.total_distance = total_distance
                    self.tour.append(0)

        for next_city in range(self.num_cities):
            if (not self.visited[next_city]) and (self.distance_matrix[current_city][next_city] != 0):
                self.visited[next_city] = True
                self.tour.append(next_city)
                self._tsp_util(next_city, num_visited + 1,
                               current_distance + self.distance_matrix[current_city][next_city])
                self.visited[next_city] = False
                self.tour.pop()

    def get_solution(self):
        return self.tour, self.total_distance


# Contoh penggunaan
if __name__ == '__main__':
    tsp = TravelingSalesmanProblem(5)  # Jumlah kota = 5

    # Menambahkan jarak antara setiap pasangan kota
    tsp.add_distance(0, 1, 10)
    tsp.add_distance(0, 2, 15)
    tsp.add_distance(0, 3, 20)
    tsp.add_distance(0, 4, 25)
    tsp.add_distance(1, 2, 35)
    tsp.add_distance(1, 3, 40)
    tsp.add_distance(1, 4, 45)
    tsp.add_distance(2, 3, 50)
    tsp.add_distance(2, 4, 55)
    tsp.add_distance(3, 4, 60)

    tsp.tsp(0)  # Memulai dari kota 0

    tour, total_distance = tsp.get_solution()
    print("Rute terpendek:")
    print(tour)
    print("Jarak total: {}".format(total_distance))
