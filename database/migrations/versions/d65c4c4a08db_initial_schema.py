"""initial schema

Revision ID: d65c4c4a08db
Revises: 
Create Date: 2025-06-20 00:41:29.053779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd65c4c4a08db'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('spotify_data', sa.JSON(), nullable=True),
    sa.Column('youtube_data', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_songs_id'), 'songs', ['id'], unique=False)
    op.create_index(op.f('ix_songs_title'), 'songs', ['title'], unique=False)
    op.create_table('fingerprints',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hash', sa.String(), nullable=True),
    sa.Column('offset', sa.Integer(), nullable=True),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fingerprints_hash'), 'fingerprints', ['hash'], unique=False)
    op.create_index(op.f('ix_fingerprints_id'), 'fingerprints', ['id'], unique=False)
    op.create_index(op.f('ix_fingerprints_offset'), 'fingerprints', ['offset'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fingerprints_offset'), table_name='fingerprints')
    op.drop_index(op.f('ix_fingerprints_id'), table_name='fingerprints')
    op.drop_index(op.f('ix_fingerprints_hash'), table_name='fingerprints')
    op.drop_table('fingerprints')
    op.drop_index(op.f('ix_songs_title'), table_name='songs')
    op.drop_index(op.f('ix_songs_id'), table_name='songs')
    op.drop_table('songs')
    # ### end Alembic commands ###
