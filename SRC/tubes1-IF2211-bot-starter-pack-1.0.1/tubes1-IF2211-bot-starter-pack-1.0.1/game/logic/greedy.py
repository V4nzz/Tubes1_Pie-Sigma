from typing import Optional
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction


class GreedyLogic(BaseLogic):
    def __init__(self):
        self.goal_position: Optional[Position] = None

    def next_move(self, board_bot: GameObject, board: Board):
        props = board_bot.properties

        if props.diamonds == 5:
            # Sudah penuh, kembali ke base
            self.goal_position = props.base
        else:
            # Cari diamond terdekat
            self.goal_position = self.find_nearest_diamond(board_bot.position, board.diamonds)

        current_position = board_bot.position

        if self.goal_position:
            delta_x, delta_y = get_direction(
                current_position.x,
                current_position.y,
                self.goal_position.x,
                self.goal_position.y,
            )
            return delta_x, delta_y
        else:
            return 0, 0  # Tidak ada langkah yang diambil

    def find_nearest_diamond(self, current_position: Position, diamonds: list[GameObject]) -> Optional[Position]:
        if not diamonds:
            return None

        nearest = min(
            diamonds,
            key=lambda d: abs(d.position.x - current_position.x) + abs(d.position.y - current_position.y)
        )
        return nearest.position
