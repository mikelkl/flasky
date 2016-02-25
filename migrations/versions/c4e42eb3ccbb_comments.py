"""comments

Revision ID: c4e42eb3ccbb
Revises: 5512ed9bd8f8
Create Date: 2016-02-25 12:42:59.798000

"""

# revision identifiers, used by Alembic.
revision = 'c4e42eb3ccbb'
down_revision = '5512ed9bd8f8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('body', sa.Text(), nullable=True),
                    sa.Column('body_html', sa.Text(), nullable=True),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.Column('disabled', sa.Boolean(), nullable=True),
                    sa.Column('author_id', sa.Integer(), nullable=True),
                    sa.Column('post_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_comments_timestamp'), 'comments', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_timestamp'), table_name='comments')
    op.drop_table('comments')
    ### end Alembic commands ###
