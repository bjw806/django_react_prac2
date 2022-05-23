import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import DeleteForeverIcon from '@material-ui/icons/DeleteForever';
import EditIcon from '@material-ui/icons/Edit';
import PostIcon from '@material-ui/icons/PostAddSharp';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '56.25%', // 16:9
	},
	link: {
		margin: theme.spacing(1, 1.5),
	},
	cardHeader: {
		backgroundColor:
			theme.palette.type === 'light'
				? theme.palette.grey[200]
				: theme.palette.grey[700],
	},
	postTitle: {
		fontSize: '16px',
		textAlign: 'left',
	},
	postText: {
		display: 'flex',
		justifyContent: 'left',
		alignItems: 'baseline',
		fontSize: '12px',
		textAlign: 'left',
		marginBottom: theme.spacing(2),
	},
}));

const Posts = (props) => {
	const { posts } = props;
	const classes = useStyles();
	if (!posts || posts.length === 0) return <p>글을 찾을 수 없습니다.</p>;
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Paper className={classes.root}>
					<TableContainer className={classes.container}>
						<Table stickyHeader aria-label="sticky table">
							<TableHead>
								<TableRow>
									<TableCell>ID</TableCell>
									<TableCell align="left">이메일</TableCell>
									<TableCell align="left">계좌번호</TableCell>
									<TableCell align="left">잔액</TableCell>
									<TableCell align="left">송금</TableCell>
								</TableRow>
							</TableHead>
							<TableBody>
								{posts.map((user) => {
									return (
										<TableRow>
											<TableCell component="th" scope="row">
												{user.id}
											</TableCell>
											<TableCell align="left">{user.email}</TableCell>

											<TableCell align="left">
												<Link
													color="textPrimary"
													href={'/user/' + user.id}
													className={classes.link}
												>
													{user.account_address}
												</Link>
											</TableCell>
											<TableCell align="left">{user.account_money}원</TableCell>
											<TableCell align="left">
												<Link
													color="textPrimary"
													href={'/transaction/transfer/' + user.account_address}
													className={classes.link}
												>
													<PostIcon></PostIcon>
												</Link>
											</TableCell>
										</TableRow>
									);
								})}
								<TableRow>
									<TableCell colSpan={5} align="right">
										<Button
											href={'/admin/create'}
											variant="contained"
											color="primary"
										>
											출금
										</Button>
									</TableCell>
								</TableRow>
							</TableBody>
						</Table>
					</TableContainer>
				</Paper>
			</Container>
		</React.Fragment>
	);
};
export default Posts;
